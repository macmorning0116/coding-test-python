import sys
input = sys.stdin.readline

def dfs(sm):
    global result
    if sm == N:
        result += 1
        return
    
    if sm > N:
        return
        
    dfs(sm+1)
    dfs(sm+2)
    dfs(sm+3)

T = int(input())
for _ in range(T):
    N = int(input())
    global result
    result = 0

    dfs(0)

    print(result)
