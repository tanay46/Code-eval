'''
Created on Jul 12, 2011

@author: tanay
'''
from sys import argv
f = open(argv[1])
text = f.readlines()

for line in text:
    nums = line.split(',')
    mult = int(nums[1])
    multcopy = mult
    big = int(nums[0])
    while big >= multcopy:
        multcopy+=mult
    print multcopy