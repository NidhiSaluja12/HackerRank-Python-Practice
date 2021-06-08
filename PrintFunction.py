n = int(input())

a=[]
for i in range (n):
    elem = i+1
    i+=1
    a.append(elem)
    print(a[i-1], end = "")
    
    
