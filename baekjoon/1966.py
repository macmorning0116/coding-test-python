import sys
from collections import*
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    inputList = list(map(int,input().split()))
    idxList = [i for i in range(0,N)]
    arr = zip(idxList,inputList)
    arr = deque(list(arr))
    q = deque()

    result = 1

    while(True):
        qMax = 0
        arrMax = 0
        if q:
            qMax = max(q, key=lambda x: x[1])[1]
        if arr:
            arrMax = max(arr, key=lambda x:x[1])[1]
        recentMax = max(qMax,arrMax)
        
        if arr: # arr이 있을 경우
            temp = arr.popleft()
            if temp[0] == M: 
                if temp[1] == recentMax:
                    print(result)
                    break
                else:
                    q.append(temp)
            else:
                if(temp[1] != recentMax):
                    q.append(temp)
                else:
                    result += 1
        
        else:
            temp = q.popleft()
            if temp[0] == M: 
                if temp[1] == recentMax:
                    print(result)
                    break
                else:
                    arr.append(temp)
            else:
                if(temp[1] != recentMax):
                    arr.append(temp)
                else:
                    result += 1
