# 단어 공부

n = input().lower()
nlist = [] 
answer = []
for i in "abcdefghijklmnopqrstuvwxyz":
  nlist.append(n.count(i))
for i in range(len(nlist)):
    if nlist[i] == max(nlist):
        answer.append(i)
if(len(answer)==1):
  print(chr(answer[0]+65))
else:
  print("?")
