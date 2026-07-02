stack1 = []
stack2 = []

q = int(input())

for _ in range(q):

    query = list(map(int, input().split()))

    if query[0] == 1:
        stack1.append(query[1])

    elif query[0] == 2:

        if not stack2:
            while stack1:
                stack2.append(stack1.pop())

        stack2.pop()

    else:

        if not stack2:
            while stack1:
                stack2.append(stack1.pop())

        print(stack2[-1])