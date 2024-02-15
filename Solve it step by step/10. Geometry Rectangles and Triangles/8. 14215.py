# 세 막대

import sys 
input = sys.stdin.readline

A, B, C = map(int, input().split())

arr = []
arr.append(A)
arr.append(B)
arr.append(C)
arr.sort()
if(arr[2] >= arr[1] + arr[0]):
    arr[2] = arr[1] + arr[0] - 1
print(sum(arr))