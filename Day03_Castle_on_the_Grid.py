import math
import os
import random
import re
import sys
from collections import deque


def minimumMoves(grid, startX, startY, goalX, goalY):
    n = len(grid)

    visited = [[False] * n for _ in range(n)]
    q = deque()

    q.append((startX, startY, 0))
    visited[startX][startY] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y, moves = q.popleft()

        if x == goalX and y == goalY:
            return moves

        for dx, dy in directions:
            nx, ny = x, y

            while True:
                nx += dx
                ny += dy

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break

                if grid[nx][ny] == 'X':
                    break

                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, moves + 1))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()