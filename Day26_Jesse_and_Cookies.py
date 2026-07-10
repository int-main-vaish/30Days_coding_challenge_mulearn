import math
import os
import random
import re
import sys

import heapq

def cookies(k, A):

    heapq.heapify(A)

    operations = 0

    while len(A) > 1 and A[0] < k:

        first = heapq.heappop(A)
        second = heapq.heappop(A)

        new_cookie = first + (2 * second)

        heapq.heappush(A, new_cookie)

        operations += 1

    if A[0] >= k:
        return operations
    else:
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
