A = set(list(map(int, input().split())))
n = int(input())

count = 0

for i in range(n):
    B = set(list(map(int, input().split())))
    if A.issuperset(B):
        count+=1
        
if count==n:
    print(True)
else:
    print(False)

