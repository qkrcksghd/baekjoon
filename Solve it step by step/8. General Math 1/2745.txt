# 진법 변환

N, B = input().split(" ")
B = int(B)
reversed_str = N[::-1]

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = 0

for i in range(len(reversed_str)):
    result += (B**i)*(number.index(reversed_str[i]))

print(result)
