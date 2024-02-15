# 소수

import sys 
input = sys.stdin.readline
M = int(input())
N = int(input())
array = []
for i in range(M, N+1):
    error = 0
    if(i>1):
        for k in range(2, i):
            if(i%k==0):
                error+=1
                break
        if(error==0):
            array.append(i)
if(len(array)>0):
    print(sum(array))
    print(min(array))
else:
    print(-1)