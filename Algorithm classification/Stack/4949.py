# 균형잡힌 세상

while True:
    a = input()
    array = []
    if(a[0] == "."):
        break
    for w in a:
        if(w=='(' or w=='['):
            array.append(w)
        elif(w==')'): 
            if(len(array)!=0 and array[-1]=='('): 
                array.pop()
            else: 
                array.append(w)
                break
        elif(w==']'):
            if(len(array)!=0 and array[-1]=='['): 
                array.pop()
            else:
                array.append(w)
                break
    if(len(array) == 0):
        print("yes")
    else:
        print("no")
