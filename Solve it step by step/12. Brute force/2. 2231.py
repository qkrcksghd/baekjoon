# 분해합
# 맞은거

import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):
    num = sum((map(int, str(i))))
    num_sum = i + num 
    if(num_sum == n):
        print(i)
        break
    if(i == n):
        print(0)
# 시간초과남

import sys
input = sys.stdin.readline
N = input()
D = []
result = 98
for result in range(10 ** (len(N) - 3), 10 ** (len(N) - 1)):
    N = int(N)
    k = sum(map(int, str(result))) + result
    if(k == N):
        D.append(result)
D.sort()
if(len(D)>0):
    print(D[0])
else:
    print(0)
