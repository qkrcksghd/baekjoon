# 대지

import sys 
input = sys.stdin.readline

N = int(input())

arr_X = []
arr_Y = []

if(N==1):
    a, b=map(int, input().split())
    print(0)
else:
    for _ in range(N):
        a, b=map(int, input().split())
        arr_X.append(a)
        arr_Y.append(b)
    print((max(arr_X) - min(arr_X)) * (max(arr_Y) - min(arr_Y)))