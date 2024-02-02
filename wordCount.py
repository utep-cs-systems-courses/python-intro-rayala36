#! /usr/bin/env python3

import sys
import os
import re
import subprocess

# Ensures that the correct number of parameters are in the command line
if len(sys.argv) != 3:
    os.write("Correct usage: wordCount.py <input text file> <output file>")
    exit()

    
def read():

    inFile = sys.argv[1]
    
    words = []
    with open(inFile, 'r') as inputFile:
        for line in inputFile:
            line = re.sub(r'[.," !;:?/-]', ' ', line)
            newWords = re.split('[ \t]', line)
            words.extend(word.lower() for word in newWords)
    return words

def write():
    words = read()
    wordsMappedToCounts = {}
    outputFile = open("output.txt", "w")
    alphabetizedList = sorted(words)
    for word in alphabetizedList:
        if word.isalpha() and word not in wordsMappedToCounts:
            wordsMappedToCounts[word] = alphabetizedList.count(word)
            outputFile.write(f"{word} {wordsMappedToCounts[word]}\n")

    outputFile.close()
            
write()




