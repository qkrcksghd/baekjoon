# 정렬 단계

import sys
input = sys.stdin.readline

array = []

for _ in range(int(input())):
    array.append(int(input()))

array.sort()

for i in range(len(array)):
    print(array[i])
