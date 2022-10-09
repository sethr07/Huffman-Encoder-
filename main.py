#!/usr/local/bin/python3
"""
Huffman Encoder
"""

# input is string of size N
# say if each char in string occupies 8 bit i.e. 8*N bits to transmit string
# Huffman can reduce this y compressiing 

# Algo:
# count number of chars in each string

import utils as ut

initial_str = "AAAAAAABCCCCCCDDEEEEE"
frequency = ut.count_elements(initial_str)
encoded_output = ut.Huffman(frequency, initial_str)

print("-------------------------------------------------")
print("-------------------------------------------------")
print("Initial String: ", initial_str)
print("HF Encoded: ", encoded_output)
print("-------------------------------------------------")
print("-------------------------------------------------")
