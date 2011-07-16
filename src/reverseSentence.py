'''
Created on Jul 12, 2011

@author: tanay
'''
from sys import argv

f = open(argv[1])
text = f.readlines()
for line in text:
    line= line.strip()
    if line != '':
        sentence = ''
        words = line.split(' ')
        words.reverse()
        for word in words:
            sentence+=' '+ word
        sentence = sentence.strip()
        print sentence


