import math
import os
import random
import re
import sys

from collections import deque

def bfs(n, m, edges, s):

    graph = [[] for _ in range(n + 1)]

    # Build graph
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    distance = [-1] * (n + 1)
    distance[s] = 0

    q = deque([s])

    while q:
        node = q.popleft()

        for neighbor in graph[node]:

            if distance[neighbor] == -1:
                distance[neighbor] = distance[node] + 6
                q.append(neighbor)

    result = []

    for i in range(1, n + 1):
        if i != s:
            result.append(distance[i])

    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
