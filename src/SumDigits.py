'''
Created on Jul 12, 2011
Given a positive integer, find the sum of its constituent digits.
@author: tanay
'''
from sys import argv
f = open(argv[1])
text = f.readlines()

for line in text:
    n = int(line)
    total = 0
    while n>0:
        total+=n%10
        n=n/10
    print total