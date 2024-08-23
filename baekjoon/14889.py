import sys
from itertools import*
input = sys.stdin.readline


N  = int(input())
arr =[[0]*(N+1)]+[[0] + list(map(int,input().split())) for _ in range(N)]
member = [i for i in range(1,N+1)]


allTeam = list(combinations(member, N//2))
teamA = allTeam[:len(allTeam)//2] 
teamB = list(reversed(allTeam[len(allTeam)//2:]))

result = set()

def isCal(arrNum):
    sum = 0
    for i in range(len(arrNum)):
        for j in range(i,len(arrNum)):
            sum += arr[arrNum[i]][arrNum[j]]
            sum += arr[arrNum[j]][arrNum[i]]
    
    return sum

for j in range(len(teamA)):
    result.add(abs(isCal(teamA[j]) - isCal(teamB[j])))


print(min(result))
