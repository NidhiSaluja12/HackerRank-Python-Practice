n = int(input())
array = []
for i in range(n):
    elem = input()
    array.append(elem)
set1 = set(array)
res = len(set1)
print(res)

