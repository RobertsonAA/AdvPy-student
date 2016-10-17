"""
:::Author:  Derrick Beckman
:::File:    ex4_1_sample.py
:::Desc:    This program will decode a caesar ciphered document given
            a cipher setting.
"""
import string

base = string.ascii_uppercase

f = open('ex4_1_data.txt')
data = f.read()

print data

def rot13Convert(data):
    """
    Takes a text string encodes/decodes it via ROT-13
    :param data: string text
    :return: encoded/decoded string
    """

    result = ''
    for letter in data:
        if letter.isalpha():
            base_position = base.find(letter.upper()) #turn letter into uppercase, based on general variable 'ascii.uppercase'
            encoded_position = (base_position - 13) % len(base) #remainder of 26 letters to always be a letter
            result += base[encoded_position]
        else:
            result += letter
    return result
