#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):

    highest = scores[0]
    lowest = scores[0]

    high_count = 0
    low_count = 0

    for score in scores[1:]:

        if score > highest:
            highest = score
            high_count += 1

        elif score < lowest:
            lowest = score
            low_count += 1

    return [high_count, low_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
