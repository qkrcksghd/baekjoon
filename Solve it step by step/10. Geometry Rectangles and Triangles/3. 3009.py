# 네 번째 점

import sys 
input = sys.stdin.readline

arr_X = []
arr_Y = []

for _ in range(3):
    a, b = map(int, input().split())
    if a not in arr_X:
        arr_X.append(a)
    else:
        arr_X.remove(a)
    
    if b not in arr_Y:
        arr_Y.append(b)
    else:
        arr_Y.remove(b)

print(*arr_X, *arr_Y)