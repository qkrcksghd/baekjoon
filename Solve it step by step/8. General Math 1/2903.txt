# 중앙 이동 알고리즘

N = int(input())

first = 2

for i in range(N):
    first+=2**i

print(first**2)