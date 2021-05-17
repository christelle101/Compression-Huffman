# Huffman Coding Data Compression

## Context

### General description

Huffman coding(also known as Huffman Encoding) is a statistical method of compressing data. Its principle is to replace a character (or symbol) by a series of bits of variable length. The underlying idea is to encode what is frequent on few bits and what is rare on longer bit sequences. It allows lossless compression, that is, as string of bits stricly identical to the original is restored by decompression. However, it requires that the frequencies of appearance of the various symbols to be coded are known(or estimated). </br>

This project solely focuses on the semi-adaptative version of the algorithm, in which the text to be encoded is read in its entirety in order to build the alphabet and determine the frequencies. </br>

This program is divided in five major steps :

### Step 1 : Determination of the alphabet and character frequencies

The alphabet will be composed of the characters present in the text provided. The order of the characters in the alphabet will be maintained by frequency ascending then in order of ASCII character encoding.

### Step 2 : Construction of the tree

The algorithm is based on a binary tree structure where all internal nodes have two successors. The leaves are labeled with the characters of the alphabet, the branches by 0 (left child) and 1 (right child). The path from the root to the leaves constitute the character codes.

### Step 3 : Encoding the text

The code for each character is obtained by a deep scan of the tree. Each character is then coded by a succession of bits and the coding of the text is obtained by concatenation. It will then be stored byte by byte in the compressed text.

### Step 4 : Determination of the compression ratio

The compression ratio measures the alorithm's performance relative to the text to compress. It is defined as the gain in volume compared to the initial volume of data (in number of bytes).

### Step 5 : Determination of the average number of storage bits for a character

**Here is an example of an application of Huffman's algorithm:**
![image](https://www.cs.princeton.edu/courses/archive/fall08/cos226/assignments/huffman.png)

## Results to be provided

The project resources contain three texts. For each one (name.txt), the program will have to generate a compressed text file (name_comp.bin) and a description file of the alphabet used with the character frequencies (name_freq.txt).
