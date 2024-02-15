# 공 넣기

basketnum, ballnum = map(int, input().split())
basket = []
for i in range(basketnum):
    basket.append(0)
for i in range(ballnum):
    quest = list(map(int, input().split()))
    for k in range(quest[0] - 1, quest[1]):
        basket[k] = quest[2]
for i in range(basketnum):
    print(basket[i], end=" ")
