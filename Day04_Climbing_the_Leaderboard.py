import math
import os
import random
import re
import sys

def climbingLeaderboard(ranked, player):
    unique_ranked = []

    for score in ranked:
        if not unique_ranked or unique_ranked[-1] != score:
            unique_ranked.append(score)

    result = []
    i = len(unique_ranked) - 1

    for score in player:
        while i >= 0 and score >= unique_ranked[i]:
            i -= 1

        result.append(i + 2)

    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
