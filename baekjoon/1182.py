import sys
input = sys.stdin.readline

def dfs(n,cnt,sm):
    global result
    if n == N:
        if sm == S and cnt > 0:
            result += 1
        return
    
    dfs(n+1, cnt+1, sm + arr[n])
    dfs(n+1, cnt, sm)
        

N,S = map(int,input().split())
arr = list(map(int,input().split()))
global result
result = 0

dfs(0,0,0)

print(result)