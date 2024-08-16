import sys
from collections import*
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    insts = list(input().rstrip())
    n = int(input())
    arrInput = input().rstrip()
    arrInput = arrInput.lstrip("[").rstrip("]")
    if arrInput != "":
        arr = deque(list(map(int,arrInput.split(","))))
    else:
        arr = []

    rev = 0
    flag = True

    instLen = len(insts)
    for idx,inst in enumerate(insts):
        if inst == "R":
            rev +=1 
        elif inst == "D":
            if arr:
                if rev%2 == 1:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print("error")
                flag = False
                break
    
    if flag:
        if rev%2 == 1:
            arr.reverse()
        print(f"[{','.join(map(str,arr))}]")



