import re

f = open('ex4_2_data.txt')
file = f.read()

search = re.search( r'(.*) 164.210.150.112 (.*?) .*', file, flags=0)

if search:
    print "Search group(): ", search.group()
    print "Search group(1): ", search.group(1)
    print "Search group(2): ", search.group(2)
else:
    print "Nothing found."


