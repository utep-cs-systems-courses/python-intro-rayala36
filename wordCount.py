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

    # Input file is the first parameter
    inFile = sys.argv[1]

    # All words will be initially stored in an array; "with" esnures opening and closing of input file
    words = []
    with open(inFile, 'r') as inputFile:
        # For each line in the file, all punctuation marks are replaced with a space
        for line in inputFile:
            line = re.sub(r'[.," !;:?/-]', ' ', line)
            # Words are placed  in a list, using space or tab as the regex
            newWords = re.split('[ \t]', line)
            words.extend(word.lower() for word in newWords)
    return words

def write():
    words = read()
    wordsMappedToCounts = {}
    outputFile = open("output.txt", "w")
    alphabetizedList = sorted(words)
    for word in alphabetizedList:
        # If a word is a alhabetic and not already in the hash table, the word and its count are added and written to output.txt.
        if word.isalpha() and word not in wordsMappedToCounts:
            wordsMappedToCounts[word] = alphabetizedList.count(word)
            outputFile.write(f"{word} {wordsMappedToCounts[word]}\n")

    outputFile.close()
            
write()




