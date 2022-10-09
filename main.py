#!/usr/local/bin/python3

import utils as ut


print("-------------------------------------------------")
print("-------------------------------------------------")
print("Welcome to Huffman Encoder")
print()
print("Enter a String of length N and let the magic happen")
val = input()
print("-------------------------------------------------")
print("-------------------------------------------------")

frequency = ut.count_elements(val)
encoded_output = ut.Huffman(frequency, val)

print("-------------------------------------------------")
print("Initial String: ", val)
print("HF Encoded: ", encoded_output)
print("-------------------------------------------------")
