import math
import os
import random
import re
import sys

def sherlockAndAnagrams(s):
    count = {}
    pairs = 0

    # Generate all substrings
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = ''.join(sorted(s[i:j]))

            if sub in count:
                count[sub] += 1
            else:
                count[sub] = 1

    # Count pairs
    for value in count.values():
        pairs += value * (value - 1) // 2

    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
