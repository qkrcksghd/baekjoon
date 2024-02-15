# A+B - 8

import sys
for i in range(0, int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{0}: {1} + {2} = {3}".format(i+1, a, b, a+b))
