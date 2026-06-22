import math
import os
import random
import re
import sys

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return n * c_lib

    graph = {i: [] for i in range(1, n + 1)}

    for u, v in cities:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    total_cost = 0

    def dfs(city):
        stack = [city]
        size = 0

        while stack:
            node = stack.pop()

            if node in visited:
                continue

            visited.add(node)
            size += 1

            for neigh in graph[node]:
                if neigh not in visited:
                    stack.append(neigh)

        return size

    for city in range(1, n + 1):

        if city not in visited:

            component_size = dfs(city)

            total_cost += c_lib
            total_cost += (component_size - 1) * c_road

    return total_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
