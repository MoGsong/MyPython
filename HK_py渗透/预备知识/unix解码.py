import crypt
def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictfile = open('dictionary.txt', 'r') #打开字典文件
    for word in dictfile.readlines():
            word = word.strip('\n') #保留原始的字符，不去空格
            cryptWord = crypt.crypt(word, salt)
            if cryptPass == cryptWord:
                print('Found passed : ', word)
                return
            print('Password not found !')
            return
def main():
 passfile = open('passwords.txt', 'r') #读取密码文件
 for line in passfile.readlines():
    user = line.split(':')[0]
    cryptPass = line.split(':')[1].strip('')
    print("Cracking Password For :", user)
 testPass(cryptPass)
if __name__ == '__main__':
 main()
