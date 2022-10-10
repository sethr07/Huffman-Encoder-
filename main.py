#!/usr/local/bin/python3
import utils as ut
import os


def mainmenu() -> int:
    print("-------------------------------------------------")
    print("-------------------------------------------------")
    print("Welcome to Huffman Encoder")
    print()
    print("----------------Select----------------------------")
    print("-----------------1. HF with String -------------------------------")
    print("-----------------2. HF with File -------------------------------")
    val = input()
    return int(val)

def hfstring():
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

def hfwithfile(infile):
    pass

key = mainmenu()

if key == 1:
    hfstring()
elif key == 2:
    pass
else:
    print("Not supported")






