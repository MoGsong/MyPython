# import socket
# import optparse
# def connScan(tgtHost, tgtPort):
#  try:
#     connSkt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     connSkt.connect((tgtHost, tgtPort))
#     print('[+]%d/tcp open' % tgtPort)
#     connSkt.close()
#  except:
#     print('[-]%d/tcp closed' % tgtPort)
# def portScan(tgtHost, tgtPorts):
#  try:
#     tgtIP = socket.gethostbyname(tgtHost)
#  except:
#     print("[-] Cannot resolve '%s': Unknown host" %tgtHost)
#     return
#  try:
#     tgtName = socket.gethostbyaddr(tgtIP)
#     print('\n[+] Scan Results for: ' + tgtName[0])
#  except:
#     print('\n[+] Scan Results for: ' + tgtIP)
#     socket.setdefaulttimeout(1)
#  for tgtPort in tgtPorts:
#     print('Scanning port ' + str(tgtPort))
#     connScan(tgtHost, int(tgtPort))
# portScan('www.baidu.com',[80,443,3389,1433,23,455])

#捕获标识
import optparse
import socket
import threading  #多线程扫描
screenLock = threading.Semaphore(value=1)   #加入锁旗标，防止线程打印输出乱序
def connScan(tgtHost, tgtPort):
 try:
    connSkt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connSkt.connect((tgtHost, tgtPort))
    connSkt.send('ViolentPython\r\n')
    results = connSkt.recv(100)
    screenLock.acquire()
    print('[+]%d/tcp open' % tgtPort)
    print('[+] ' + str(results))

 except:
    print('[-]%d/tcp closed' %tgtPort)
    screenLock.acquire()
 finally:
     screenLock.release()
     connSkt.close()

def portScan(tgtHost, tgtPorts):
     try:
         tgtIP = socket.gethostbyname(tgtHost)
     except:
         print( "[-] Cannot resolve '%s': Unknown host" %tgtHost)
         return
     try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: ' + tgtName[0])
     except:
        print('\n[+] Scan Results for: ' + tgtIP)
     socket.setdefaulttimeout(1)
     for tgtPort in tgtPorts:
        print('Scanning port ' + str(tgtPort))
        t = threading.Thread(target=connScan, args=(tgtHost,int(tgtPort)))  # target=connScan 建立线程扫描
        t.start()
        # connScan(tgtHost, int(tgtPort))

def main():  #tgtHost, tgePort
    parser = optparse.OptionParser('usage %prog –H < target host > -p < target port > ')
    parser.add_option('-H', dest='tgtHost', type='string',
                      help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='int',
                      help='specify target port')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = options.tgtPort
    args.append(tgtPort)
    if (tgtHost == None) | (tgtPort == None):
        print('[-] You must specify a target host and port[s]!')
        exit(0)
    portScan(tgtHost, args)

if __name__ == '__main__':
    main()   #'-H www.qq.com -p 80 21 25 443 53'


