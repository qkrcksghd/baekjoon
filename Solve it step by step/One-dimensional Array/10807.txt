# 개수 세기

n = int(input())
n_list = list(map(int, input().split()))
if(n != len(n_list)):
    print("같지않음")
else:
    print(n_list.count(int(input())))
