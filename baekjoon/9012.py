import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    arr = input().strip()
    stack = []

    for char in arr:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)

    if not stack:
        print("YES")
    else:
        print("NO")
