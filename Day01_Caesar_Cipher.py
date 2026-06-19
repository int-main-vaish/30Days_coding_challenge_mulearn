import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    r=""
    for ch in s:
        if ch.islower():
            r += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        elif ch.isupper():
            r += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
        else:
            r += ch
    return r
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()