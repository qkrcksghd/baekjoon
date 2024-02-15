# 알람 시계

def times(a, b):
    if(b<0):
        a-=1
        b+=60
    if(a<0):
        a+=24
    return a, b
year, minute = map(int, input().split())
minute-=45
year, minute = times(year, minute)
print(year, minute)
