# 주사위 세개

a = list(map(int, input().split()))
a.sort(reverse=True)
#3개 같음
if(a[0] == a[1] == a[2]):
    print(10000+(a[0]*1000))
#2개 같음
elif(a[0]==a[1] or a[0]==a[2] or a[1]==a[2]):
    print(1000+(a[1]*100))
#다다름
else:
    print(a[0]*100)
