import numpy
N,M = map(int, input().split())

arr = numpy.array([input().split() for i in range (N)], int)

transpose = numpy.transpose(arr)
print(transpose)
flatten = arr.flatten()
print(flatten)



