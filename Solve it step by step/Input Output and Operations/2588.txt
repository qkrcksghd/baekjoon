# 곱셈

a = int(input())
b = int(input())
list = [b%10, (b//10) - (b//100 * 10), b//100, b]
for i in range(0, 4):
    print(list[i] * a)
