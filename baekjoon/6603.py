import sys
from itertools import*
input = sys.stdin.readline

def dfs(n,cnt):
    global result, visit
    if cnt == 6:
        temp = []
        for i,v in enumerate(visit):
            if v== 1:
                temp.append(tempList[i])
        result.append(temp)
        return

    if n == N:
        return
    
    # 숫자 추가o

    visit[n] = 1
    dfs(n+1, cnt+1)
    visit[n] = 0

    # 숫자 추가x
    dfs(n+1, cnt)

while True:
    arr = list(map(int,input().split(" ")))
    N = arr[0]
    global result
    global visit
    visit = [0]*N
    result = list()
    if N != 0:
        tempList = arr[1:]
        dfs(0,0)

        for arr in result:
            print(f"{' '.join(map(str,arr))}")
        
        print(" ")
    else:
        break

