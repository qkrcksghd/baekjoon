# 오븐 시계

def times(a, b):
    if(b>=60):
        a+=1
        b-=60
    if(a>=24):
        a-=24
    return a, b
year, minute = map(int, input().split())
sum = int(input())
minute += sum
while True:
    year, minute = times(year, minute)
    if(minute<60):
        break
print(year, minute)
