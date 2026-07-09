import math
import os
import random
import re
import sys

def nonDivisibleSubset(k, s):

    rem = [0] * k

    # Count remainders
    for num in s:
        rem[num % k] += 1

    count = min(rem[0], 1)

    for i in range(1, (k // 2) + 1):

        if i != k - i:
            count += max(rem[i], rem[k - i])

    if k % 2 == 0:
        count += 1 if rem[k // 2] > 0 else 0

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
