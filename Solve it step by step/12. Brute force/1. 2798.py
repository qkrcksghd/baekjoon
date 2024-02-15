# 블랙잭

import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
a = list(combinations(arr, 3))
result = []
s = 0

for i in range(len(a)):
    result.append(sum(a[i]))
result.sort()


for i in result:
    if(i==M):
        s=i
        break
    elif(i>M):
        break
    s=i
print(s)
