# 색종이

n = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):

    x,y = map(int,input().split())
    for row in range(x,x + 10):
        for col in range(y,y + 10):

            paper[row][col] = 1
result = 0
for i in paper:
    result += sum(i)

print(result)