import re

for IPV4 in open('ex4_2_data.txt'):
    iprange = '^(([0-6]|0)?([0-6]|0)?([0-6]|0)\.([0-6]|0)?([0-6]|0)?([0-6]|0)\.([0-6]|0)?([0-6]|0)?([0-6]|0)\.([0-6]|0)?([0-6]|0)?([0-6]|0))$'
    IP = re.findall(iprange, IPV4)
    if IP:
        print IPV4



    #if IP:

#for IPV4 in open('ex4_2_data.txt'):
     #iprange = '^(([0-6]|0)?([0-6]|0)?([0-6]|0)\.([0-6]|0)?([0-6]|0)?([0-6]|0)\.([0-6]|0)?([0-6]|0)?([0-6]|0)\.([0-6]|0)?([0-6]|0)?([0-6]|0))$'
     #IP = re.findall(iprange, IPV4)
#
# lines = len(IP.readlines())
#    if IP:
#        print IPV4

        #filename = "somefile.txt"
        #myfile = open(filename)
        #lines = len(myfile.readlines())
        #print "There are %d lines in %s" % (lines, filename)
        #count = IP.splitlines()
    #print (len(count))

    #return pattern.match(IP)

    #return IPRANGE.match(IPV4)
    #IP = re.findall(IPRANGE, IPV4)
    #if IP:
        #print IPV4

#in open('ex4_2_data.txt')

#def main(file, size):
#    tracker = defaultdict(int)
#    with open('ex4_2_data.txt', 'w') as fout:
#        for i in xrange(size):
#            try:
#                fout.write(gen_line(tracker))
#                fout.write('\n')
#            except valueError as e:
#                pass
    #f = open('ex4_2_data.txt')
    #data = f.read()
    #ip = re.findall(IPRANGE, data)

#if __name__ == "__main__":
    #main()

    #with open (file, 'w') as fout:




#IP = re.findall(IPRANGE, data)
#for IP in IPRANGE:
#    lprint IP


