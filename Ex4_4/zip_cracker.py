import zipfile
import itertools
import argparse
import string

def main():
    zfile = zipfile.ZipFile('ex4_4.zip', 'r')
    #start = time.time()
    #print ("Starting crack at ()".format(time.strftime('%j: %H:%M:%S', time.localtime(start))))
    #print ('.', end = '')
    for i, p in enumerate(gen_pass(maxval=4)):
        #if not i % 1000: print'.', end = ''
        #if not i % 10000: print('\n{}'.format(i / 100000), end='')
        if p == 's@f3': print('found s@f3')
        try:
            zfile.extractall(pwd=p)
            print('\nThe password is {}'.format (p))
            print('That took {} seconds'.format(time.time()-start))
            exit(0)
        except RuntimeError:
            pass
        except Exception as e:
            pass

def gen_pass(minval=3, maxval=4):
    letters = string.ascii_lowercase
    numbers = '1234567890'
    symbols = '!@#'
    characters = list(letters) + list(numbers) + list(symbols)
    while maxval >= minval:
        for p in itertools.product(characters, repeat=maxval):
            yield ''.join(p)
    try:
        zFile.extractall(pwd=password)
        return
    except:
        return

if __name__ == "__main__":
    main()





