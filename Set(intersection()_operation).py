n1 = int(input())
array1 = list(map(int, input().split()))
n2 = int(input())
array2 = list(map(int, input().split()))
set1 = set(array1)
set2 = set(array2)

intersection1 = set1.intersection(set2)
result = list(intersection1)
print(len(result))

