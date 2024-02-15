# 숫자의 합

num = int(input())
a = input()
if num==len(a):
  print(sum(int(a[i]) for i in range(len(a))))
