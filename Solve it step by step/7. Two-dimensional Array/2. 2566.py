# 최댓값

nlist1 = []
result = 0
max_row = 0
for _ in range(9):
    tmp = list(map(int, input().split()))
    nlist1.append(tmp)
for row in range(0, 9):
    if result < max(nlist1[row]):
        result = max(nlist1[row])
        max_row = row
print(result)
print(max_row + 1, nlist1[max_row].index(max(nlist1[max_row])) + 1)
