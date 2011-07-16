'''
Created on Jul 16, 2011
Prints the nth Fibonacci number
@author: tanay
'''
from sys import argv
f = open(argv[1])
text = f.readlines()

def fibo(n):
    if n<2: 
        return n
    else: 
        return fibo(n-1)+fibo(n-2)

for line in text:
    n = int(line)
    x = fibo(n)
    print x