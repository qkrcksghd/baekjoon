# 별 찍기 - 1

import sys
num = int(sys.stdin.readline())
for i in range(1, num+1):
    for i in range(0, i):
        print("*", end="")
    print("")
