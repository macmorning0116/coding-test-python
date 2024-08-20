import sys
input = sys.stdin.readline

M,N = map(int,input().split())

def decimalCheck(num):
    if num == 1:
        return False
    
    result = True
    for i in range(2, (int)(num**0.5) + 1):
        if num%i == 0:
            result = False
            break
    
    return result


for num in range(M,N+1):
    if decimalCheck(num):
        print(num)

