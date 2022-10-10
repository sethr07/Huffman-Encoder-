#!/usr/local/bin/python3
import utils as ut
import os

print("-------------------------------------------------")
print("-------------------------------------------------")
print("Welcome to Huffman Encoder")
print()

print("----------------Select----------------------------")
print("-----------------1. HF with String -------------------------------")
print("-----------------2. HF with File -------------------------------")
val = input()


if val == 1:
    print("Enter a String of length N and let the magic happen")
    val = input()
    print("-------------------------------------------------")
    print("\n\n")
    frequency = ut.count_elements(val)
    encoded_output, size_before, size_after, tree = ut.huffman(frequency, val)
    print("----------------RESULTS--------------------------")
    print("Initial String: ", val)
    print("HF Encoded: ", encoded_output)
    print("-------------------------------------------------")
    print("Do you want information about Compression? (y/n)")
    val = input()
    if val == 'y':
        print("-------------------INFO--------------------------")
        print("Entropy before Compression (bits): ", size_before)
        print("Entropy after Compression (bits): ", size_after)
        print("-------------------------------------------------")
elif val == 2:
    print("Enter a File Name")
    val = input()
    




