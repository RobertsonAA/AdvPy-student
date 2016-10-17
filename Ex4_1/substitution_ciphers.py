import string


def main():
    class AtBash:

        def __init__(self):
            self.alphabets = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_+|:"<>-=[];,.?/`'

        def encode(self, plaintext):
            cipher = ""
            for i in plaintext:
                index = self.alphabets.index(i)
                cipher += self.alphabets[abs(len(self.alphabets) - index - 1) % len(self.alphabets)]
            return cipher

        def decode(self, ciphertext):
            return self.encode(ciphertext)

    if __name__ == "__main__":
        atbash = AtBash()

        enc = atbash.encode("Hello World!")
        print(enc)

        dec = atbash.decode(enc)
        print(dec)

if __name__ == "__main__":
    main()









