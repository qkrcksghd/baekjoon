# 대표값2

import sys
input = sys.stdin.readline

array = []

for _ in range(5):
    array.append(int(input()))

array.sort()

print((sum(array)) // 5)
print(array[2])
