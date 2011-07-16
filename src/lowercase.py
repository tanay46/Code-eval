'''
Created on Jul 12, 2011
Given a string converts it into lowercase.
@author: tanay
'''
from sys import argv
f = open(argv[1])
text = f.readlines()

for line in text:
    line = line.strip()
    print line.lower()