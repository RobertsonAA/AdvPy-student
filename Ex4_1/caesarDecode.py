import argparse
import string
import base64
from Crypto.Cipher import AES

def main():
    with open('ex4_1_data.txt') as fin:
        a = fin.read()

        b = caesarDecode(a, 6)
        c = b[158:]
        d = atbash(c)
        e = d[129:]
        f = base64Decode(e)
        g = f[196:]
        h = AESDecode(g, '9b4609b17fea63f3f3f067fc2f465c6e')

        print h

            #print z
            #z = atbash(y)

            #for i in xrange(len(string.ascii_lowercase)):
            #print("{}: {}".format(i,caesarDecode(a, i)))

def caesarEncode(data, shift):
    result = ''
    for letter in data:
        if letter.isupper():
            base_position = string.ascii_uppercase.find(letter)
            encoded_position = (base_position + shift) % 26
            result += string.ascii_uppercase[encoded_position]
        elif letter.islower():
            base_position = string.ascii_lowercase.find(letter)
            encoded_position = (base_position + shift) % 26
            result += string.ascii_lowercase[encoded_position]
        else:
            result += letter
    return result

def caesarDecode(data, shift):
    return caesarEncode(data, shift * -1)

def atbash(data):
    result = ''
    for letter in data:
        if letter.isupper():
            base_position = string.ascii_uppercase.find(letter)
            encoded_position = ((base_position + 1) * -1)
            result += string.ascii_uppercase[encoded_position]
        elif letter.islower():
            base_position = string.ascii_lowercase.find(letter)
            encoded_position = ((base_position + 1) * -1)
            result += string.ascii_lowercase[encoded_position]
        else:
            result += letter
    return result

def base64Encode(data):
    return base64.encode(data)

def base64Decode(data):
    return base64.b64decode(data)

def AESDecode(data, key):
    aes = AES.new(key)
    return aes.decrypt(data)

if __name__ == "__main__":
    main()