n1 = int(input())
array1 = list(map(int, input().split()))

n2 = int(input())
array2 = list(map(int, input().split()))

set1 = set(array1)
set2 = set(array2)

symm_difference = set1.symmetric_difference(set2)

result = list(symm_difference)
print(len(result))

