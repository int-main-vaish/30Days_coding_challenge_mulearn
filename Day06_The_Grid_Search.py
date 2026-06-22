import math
import os
import random
import re
import sys

def gridSearch(G, P):
    R = len(G)
    r = len(P)
    c = len(P[0])

    for i in range(R - r + 1):
        pos = G[i].find(P[0])

        while pos != -1:
            found = True

            for j in range(1, r):
                if G[i + j][pos:pos + c] != P[j]:
                    found = False
                    break

            if found:
                return "YES"

            pos = G[i].find(P[0], pos + 1)

    return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
