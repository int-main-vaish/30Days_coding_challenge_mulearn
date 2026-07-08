import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    freq = {}
    pairs = 0

    for sock in ar:
        freq[sock] = freq.get(sock, 0) + 1

    for count in freq.values():
        pairs += count // 2

    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
