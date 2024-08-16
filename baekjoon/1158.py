n,k = map(int,input().split())
arr = [i for i in range(1,n+1)]
result = []
num = 0

for _ in range(n):
    num += (k-1)
    if num > len(arr) - 1:
        num %= len(arr)
    
    result.append(arr.pop(num))

print("<" + ", ".join(map(str,result)) + ">")


