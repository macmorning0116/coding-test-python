import sys
input = sys.stdin.readline

n = int(input())
arr = []
stack = []
out = []
global num
num = 1
flag = True

for _ in range(n):
    arr.append(int(input()))

def pushMethod(before, recent):
    global num
    for _ in range(before, recent+1):
        stack.append(num)
        num += 1
        out.append(1)



for i in arr:
    if not stack or (stack and stack[-1] < i):
        pushMethod(num, i) 

    if stack and stack[-1] == i:
        stack.pop()
        out.append(0)
    
    elif stack and stack[-1] > i:
        flag = False
        break


if(flag):
    for i in out:
        if i == 1:
            print("+")
        else:
            print("-")
else:
    print("NO")

