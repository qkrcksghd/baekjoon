# 세탁소 사장 동혁

T = int(input())

change =[25, 10, 5, 1]

for _ in range(T):
    C = int(input())
    for k in change:
        print(C // k, end=" ")
        C = (C - (k * (C // k)))
    print()