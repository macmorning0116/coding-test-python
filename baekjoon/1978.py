import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

def decimalCheck(num):
    if num == 1:
        return False
    result =  True
    for i in range(2, (int)(num**0.5) + 1):
        if num%i == 0:
            result = False
            break
    return result

cnt = 0
for i in arr:
    if(decimalCheck(i)):
        cnt += 1

print(cnt)