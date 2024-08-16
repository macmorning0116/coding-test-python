import sys
from collections import*
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    inputList = list(map(int,input().split()))
    idxList = [i for i in range(0,N)]
    arr = deque(list(zip(idxList,inputList)))

    result = 1
    maxNum = max(arr, key= lambda x: x[1])[1]

    while True:
        idx, val = arr.popleft()
        if idx == M and val == maxNum:
            print(result)
            break

        elif val == maxNum:
            maxNum = max(arr, key= lambda x:x[1])[1]
            result += 1
        
        else:
            arr.append((idx,val))
        
