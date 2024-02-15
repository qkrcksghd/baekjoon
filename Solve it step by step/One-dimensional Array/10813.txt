# 공 바꾸기

basketnum, ballnum = map(int, input().split())
basket = list(range(1, basketnum+1))
for _ in range(ballnum):
    one, two = map(lambda x: int(x) - 1, input().split())
    basket[one], basket[two] = basket[two], basket[one]
print(*basket)
