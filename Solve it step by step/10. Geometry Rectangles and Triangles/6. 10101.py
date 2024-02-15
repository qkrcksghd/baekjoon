# 삼각형 외우기

import sys 
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

if(A+B+C != 180):
    print("Error")
else:
    if(A==B==C):
        print("Equilateral")
    elif(A==B or B==C or A == C):
        print("Isosceles")
    else:
        print("Scalene")