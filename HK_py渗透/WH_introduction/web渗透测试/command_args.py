import optparse
parser = optparse.OptionParser()  # 初始化
parser.usage = "command_ars.py - u user_file"
parser.add_option("-u", "--user_file", help="read username from file", action="store",type="string",dest="user_file") # 添加参数 属性  metavar="FILE",
(options, args) = parser.parse_args()   # 保存
# print(options.user_file)  # 输出



"""def main():
    parser = optparse.OptionParser("usage %prog –H < target host > -p < target port > ")
    parser.add_option('-H', dest='tgtHost', type='string',
                      help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string',
                      help='specify target port')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = options.tgtPort
    args.append(tgtPort)
    if (tgtHost == None) | (tgtPort == None):
        print('[-] You must specify a target host and port[s]!')
    exit(0)
    for tgport in args:
        nmapScan(tgtHost, tgport)"""