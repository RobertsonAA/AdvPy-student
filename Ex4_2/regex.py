import re

for data in open('ex4_2_data.txt'):
    iprange = '^(10)' #\.(0|[0-6)(0|[0-6])(0|[0-6])' #(0|[0-6)(0|[0-6])(0|[0-6])\.(0|[0-6)(0|[0-6])(0|[0-6])$'
    IP = re.findall(iprange, data)
    try:
        if IP in iprange:
            print IP
    except:
        print "Loop failed"




