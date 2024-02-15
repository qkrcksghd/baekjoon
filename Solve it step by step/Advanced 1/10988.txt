# 팰린드롬인지 확인하기

n = input()
result = 1
for i in range(len(n)):
  if(n[i] != n[len(n)-i-1]):
    result = 0
print(result)