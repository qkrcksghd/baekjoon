# 영수증

totalPrice = int(input())
sum = 0
for i in range(0, int(input())):
    price, count = map(int, input().split())
    sum += price * count
if(totalPrice==sum):
    print("Yes")
else:
    print("No")
