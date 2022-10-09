#!/usr/local/bin/python3

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
