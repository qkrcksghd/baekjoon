# 약수들의 합

import sys 
input = sys.stdin.readline
while True:
    N = int(input())
    if(N==-1):
        break
    array = []
    for i in range(1, N):
        if(N%i==0):
            array.append(i)
    if sum(array) == N:
        print(N,"=",end=" ")
        print(*array,sep=" + ")
    else:
        print("{0} is NOT perfect.".format(N))