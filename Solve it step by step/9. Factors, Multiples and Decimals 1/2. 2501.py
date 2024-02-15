# 약수 구하기

import sys 
input = sys.stdin.readline
N, K = map(int, input().split())
array = []
num = 1
while True:
    if(num == N):
        break
    if(N%num==0):
        array.append(num)
    num+=1
array.append(num)
if(len(array) < K):
    print(0)
else:
    print(array[K-1])