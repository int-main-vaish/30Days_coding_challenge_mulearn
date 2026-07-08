import math
import os
import random
import re
import sys

def pickingNumbers(a):
    freq = {}

    for num in a:
        freq[num] = freq.get(num, 0) + 1

    max_len = 0

    for num in freq:
        length = freq[num] + freq.get(num + 1, 0)

        if length > max_len:
            max_len = length

    return max_len

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
