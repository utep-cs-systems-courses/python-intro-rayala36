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
            # Consecutive spaces are replaced with a single space
            line = re.sub(r'\s+', ' ', line)
            line = re.sub(r'[.," !;:?/-]', ' ', line)
            # Words are placed  in a list with the "split" function
            newWords = line.split()
            words.extend(word.lower() for word in newWords)
    return words

def write():
    # Array of all words in the input file will be taken as output from the "read" function
    words = read()
    wordsMappedToCounts = {}
    outputFile = open("output.txt", "w")
    for word in words:
        if word.isalpha():
            # For all alphabetical words, if the word is not present in the dictionary, it will be given
            # a default value of zero and will be incremented by one.  Otherwise, the word's current count
            # value will be incremented by one.
            wordsMappedToCounts[word] = wordsMappedToCounts.get(word, 0) + 1
    alphabetizedDict = sorted(wordsMappedToCounts.items())
    
    for word, wordsMappedToCounts[word] in alphabetizedDict:
        outputFile.write(f"{word} {wordsMappedToCounts[word]}\n")

    outputFile.close()
            
write()




