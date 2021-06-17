n = int(input())
A = set(list(map(int, input().split())))

N = int(input())

for i in range(N):
    a, b = input().split()
    B = set(list(map(int, input().split())))
    
    if a == 'intersection_update':
        A.intersection_update(B)
        
    elif a == 'update':
        A.update(B)
        
    elif a == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
        
    elif a == 'difference_update':
        A.difference_update(B)
        
result = list(A)
        
print(sum(result))
        

