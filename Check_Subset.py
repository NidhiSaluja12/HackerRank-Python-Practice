T = int(input())        #Test Case
for i in range(T):
    N1 = int(input())
    A = set(list(map(int, input().split())))
    N2 = int(input())
    B = set(list(map(int, input().split())))
    set1 = A.difference(B)
    if len(set1)==0:
        print("True")
    else:
        print("False")
    
    
