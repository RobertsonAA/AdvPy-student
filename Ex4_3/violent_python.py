import crypt

def testPass(cryptPass):
    ctype = cryptPass.split("$")[1]
    salt = cryptPass.split("$")[2]
    insalt = "$" + ctype + "$" + salt + "$"
    print insalt

    dictFile = open('password.lst','r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,insalt)
        if (cryptWord == cryptPass):
            print "[+] Found Password: "+word+"\n"
            return
    print "[-] Password Not Found.\n"
    return

def main():
    passFile = open('ex4_3_data.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print "[*] Cracking Password For: "+user
            testPass(cryptPass)

if __name__ == "__main__":
    main()