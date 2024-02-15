# 킹, 퀸, 룩, 비숍, 나이트, 폰

result = [1,1,2,2,2,8]
nlist = list(map(int, input().split()))
for i in range(0, 6):
  if(nlist[i] == result[i]):
    nlist[i] = 0
  else:
    nlist[i] = result[i] - nlist[i]
  print(nlist[i], end=" ")
