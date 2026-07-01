import math
import os
import random
import re
import sys

def minimumNumber(n, password):

    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    missing = 0

    if not any(ch in numbers for ch in password):
        missing += 1

    if not any(ch in lower_case for ch in password):
        missing += 1

    if not any(ch in upper_case for ch in password):
        missing += 1

    if not any(ch in special_characters for ch in password):
        missing += 1

    return max(missing, 6 - n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
