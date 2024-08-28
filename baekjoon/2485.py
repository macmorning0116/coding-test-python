import sys
input = sys.stdin.readline

N = int(input())
arr = list(int(input()) for _ in range(N))
distance = []

def gcd(a,b):
    while b > 0:
        a,b = b, a%b
    return a

for i,v in enumerate(arr):
    if i > 0:
        distance.append(v - arr[i-1])

checkDis = set(distance)
checkDis = list(checkDis)
checkDis.sort()
comMax = checkDis[0]

if len(checkDis) == 1:
    comMax = checkDis[0]
else:
    for i,v in enumerate(checkDis):
        if i > 0:
            comMax = gcd(comMax,checkDis[i])

result = 0

for dis in distance:
    if dis > comMax:
        result += ((dis-comMax)//comMax)

print(result)