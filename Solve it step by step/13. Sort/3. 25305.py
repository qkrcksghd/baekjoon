# 커트라인

import sys
input = sys.stdin.readline

N, k = map(int, input().split())

array = list(map(int, input().split()))

array.sort(reverse=True)

print(array[k-1])
