import math
import os
import random
import re
import sys

def componentsInGraph(gb):

    graph = {}

    # Build adjacency list
    for u, v in gb:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)

    visited = set()

    smallest = float('inf')
    largest = 0

    for node in graph:

        if node not in visited:

            stack = [node]
            visited.add(node)
            size = 0

            while stack:

                current = stack.pop()
                size += 1

                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

            smallest = min(smallest, size)
            largest = max(largest, size)

    return [smallest, largest]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
