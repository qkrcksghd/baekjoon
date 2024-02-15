# X보다 작은 수

count, value = map(int, input().split())
nlist = list(map(int, input().split()))
for i in range(0, count):
    if(nlist[i] < value):
        print(nlist[i], end=" ")
