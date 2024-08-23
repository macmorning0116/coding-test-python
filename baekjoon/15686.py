import sys
from itertools import*
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

homes = []
chickens = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            homes.append((i,j))
        elif arr[i][j] == 2:
            chickens.append((i,j))

sChk = list(combinations(chickens, M))
result = set()

def homeToChick(home,chicken):
    temp = []
    hi,hj = home
    for chk in chicken:
        ci,cj = chk
        temp.append(abs(ci-hi) + abs(cj-hj))
    
    return min(temp)

def homeToChicken(chicken):
    sum = 0
    for home in homes:
        sum += homeToChick(home,chicken)

    return sum


for chicken in sChk:
    result.add(homeToChicken(chicken))

print(min(result))