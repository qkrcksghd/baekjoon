# 행렬 덧셈

a,b = map(int, input().split())
nlist1, nlist2 = [], []
for _ in range(a):
    tmp = list(map(int, input().split()))
    nlist1.append(tmp)
for _ in range(a):
    tmp = list(map(int, input().split()))
    nlist2.append(tmp)
for row in range(a):
    for col in range(b):
        print(nlist1[row][col] + nlist2[row][col], end=' ')
    print()
