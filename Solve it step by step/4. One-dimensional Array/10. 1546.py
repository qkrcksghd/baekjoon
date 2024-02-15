# 평균

nlist_size = int(input())
nlist = list(map(int, input().split()))
if(nlist_size == len(nlist)):
  nlist.sort(reverse=True)
  max = nlist[0]
  average = 0
  for i in range(nlist_size):
    nlist[i] = nlist[i]/max * 100
    average += nlist[i]
  print(average / nlist_size)
