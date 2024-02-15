# 윤년

def dbssus(a):
    if(a%4==0):
        if(a%100!=0 or a%400==0):
            return 1
    return 0
a = int(input())
print(dbssus(a))
