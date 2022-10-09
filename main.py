#!/usr/local/bin/python3
import utils as ut

print("-------------------------------------------------")
print("-------------------------------------------------")
print("Welcome to Huffman Encoder")
print()
print("Enter a String of length N and let the magic happen")
val = input()
print("-------------------------------------------------")
print("\n\n")

frequency = ut.count_elements(val)
encoded_output = ut.huffman(frequency, val)

print("----------------RESULTS--------------------------")
print("Initial String: ", val)
print("HF Encoded: ", encoded_output)
print("-------------------------------------------------")
