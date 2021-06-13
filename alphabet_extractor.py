#libraries imports

import math
import heapq

file = input("Enter your file name: ")
fileOpen = open(file, "r")
fileContent = fileOpen.read()


#returns the file content
def textReader(file):
    return fileContent


#print(textReader("textesimple.txt"))


#returns the ASCII code of each character present in the text
def ASCII_extractor(text):
    for c in text:
        print(c, ord(c))

print(ASCII_extractor(fileContent))
