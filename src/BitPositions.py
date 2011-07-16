'''
Created on Jul 12, 2011
Given a number n and two integers p1,p2 determines if the bits in position p1 and p2 are the same or not. Positions p1,p2 and 1 based.
@author: tanay
'''
from sys import argv
f = open(argv[1])
text = f.readlines()

for line in text:
    nums = [int(x) for x in line.split(',')]
    bina = bin(nums[0])
    if bina[len(bina)-nums[1]]==bina[len(bina)-nums[2]]:
        print "true"
    else: print "false"