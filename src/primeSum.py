'''
Created on Jul 12, 2011

@author: tanay
'''
from math import sqrt
def isPrime(n):
    if n==0 or n==1: return False
    elif n==2 or n==3: return True
    else:
        s = int(sqrt(n))
        for x in range(2,s+1):
            if n%x==0:
                return False
        return True
sum = 0
number = 0
start = 0
while number<1000:
    if isPrime(start):
        sum+=start
        number+=1
    start+=1

print sum
        
