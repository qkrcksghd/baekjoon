# 삼각형과 세 변

import sys 
input = sys.stdin.readline

while True:
    arr = []
    A, B, C = map(int, input().split())

    if(A==B==C==0):
        break

    arr.append(A)
    arr.append(B)
    arr.append(C)
    arr.sort()
    if(arr[2] < arr[1] + arr[0]):
        if(A==B==C):
            print("Equilateral")
        elif(A==B or B==C or A == C):
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")