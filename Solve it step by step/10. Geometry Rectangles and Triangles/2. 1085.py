# 직사각형에서 탈출

import sys 
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

arr = []
arr.append(w-x)
arr.append(h-y)
arr.append(x)
arr.append(y)
arr.sort()
print(arr[0])