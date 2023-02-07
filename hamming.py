#!/usr/bin/env python3
# hamming.py
import sys


def hamming(string1, string2):
    """
    Takes 2 arguments: takes 2 strings
    Returns the hamming distance between those strings
    """
    count = 0
    for x in range(len(string1)):
        if string1[x] != string2[x]:
            count += 1
    return count
        

if __name__ == "__main__":
    string1 = sys.argv[1]
    string2 = sys.argv[2]
    
    # Check to make sure both strings are the same length or raise exception
    if len(string1) != len(string2):
        raise Exception("This script requires 2 strings of the same length.")

    answer = hamming(string1, string2)
    print(f"{string1}\t{string2}\t{answer}")
