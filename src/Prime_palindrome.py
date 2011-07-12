'''
Created on Jul 12, 2011

@author: tanay
'''
from math import sqrt
def isPrime(n):
    for x in range(2,int(sqrt(n))):
        if n%x==0:
            return False
    return True

def isPalindrome(n):
    return str(n)==str(n)[::-1]

found = False
i = 1000
while not found:
    if isPrime(i) and isPalindrome(i):
        found = True
        print i
    else:
        i = i-1
