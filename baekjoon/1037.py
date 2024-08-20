import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

maxNum = max(arr)
result = maxNum

def countDivisors(num):
    cnt = 0
    for i in range(1, (int)(num**0.5) + 1):
        if num%i == 0:
            if i*i == num:
                cnt +=1
            else:
                cnt += 2

    return cnt

def checking(result):
    result += maxNum
    while True:
        for num in arr:
            if result%num != 0:
                result += maxNum
                break
        else:
            break
    return result

while True:
    result = checking(result)
    cnt = countDivisors(result) - 2
    if cnt == N:
        break


print(result)
    


# 약수의 개수 세기
# num = 10
# arr = []

# for i in range(1, (int)(num**0.5)+1):
#     if num%i == 0:
#         arr.append(i)

# print(arr)
