import sys
input = sys.stdin.readline

N = int(input())
arr = []
temp = [i for i in range(1,N+1)] 
result = 0

def primeArr(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,(int)(n**0.5) + 1):
            if n%i == 0:
                return False
    return True

for num in temp:
    if primeArr(num):
        arr.append(num)

for i in range(len(arr)):
    temp = 0
    for j in range(i,len(arr)):
        temp += arr[j]
        if temp == N:
            result += 1
            break
        elif temp > N:
            break

print(result)
    




