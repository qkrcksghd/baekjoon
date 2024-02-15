# 너의 평점은

gkrwja = [("A+", 4.5), ("A0", 4.0), ("B+", 3.5), ("B0", 3.0) , ("C+", 2.5)
          ,("C0", 2.0), ("D+", 1.5), ("D0", 1.0), ("F", 0.0)]
sum = 0
rotn = 0
for _ in range(20):
  a,b,c = input().split()
  b = float(b)
  if(c!="P"):
    rotn+=b
  for i in range(9):
    if(c==gkrwja[i][0]):
      sum+=b*gkrwja[i][1]
print(sum/rotn)
