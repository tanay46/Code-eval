'''
Created on Jul 16, 2011

@author: tanay
'''
from sys import argv
f = open(argv[1])
text = f.readlines()
sum=0
for line in text:
    n = int(line)
    sum+=n
print sum