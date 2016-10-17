import crypt
#from __future__ import print_function

def testPass(cryptPass):
    salt = cryptPass[0:2]

    dictFile = open('password.lst')
    for word in dictFile.readlines():
        word = word.strip()
        cryptWord = crypt.crypt(word.salt)
        if (cryptWord == cryptPass):
            print "Found Password: " + word + "\n"
            return

    print "[-] Password Not Found.\n"
    return

def main():
    passFile = open('ex4_3_data.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip('')
            print "Cracking Password For: " + user
            testPass(cryptPass)

if __name__ == "__main__":
    main()
