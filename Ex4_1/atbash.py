import string

def main():
    with open('ex4_1_data.txt') as fin:

    a = fin.read()


def atbash(data):
    result = ''
    for letter in data:
        if letter.isupper():
            base_position = string.ascii_uppercase.find(letter)
            encoded_position = ((base_position + 1) * -1)
            result += string.ascii_uppercase(encoded_position)
        elif letter.islower():
            base_position = string.ascii_lowercase.find(letter)
            encoded_position = ((base_position + 1) * -1)
            result += string.ascii_lowercase[encoded_position]
        else:
            result += letter
    return result

if __name__ == "__main__":
    main()