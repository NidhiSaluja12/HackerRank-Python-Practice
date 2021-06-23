import numpy
N,M,P = map(int, input().split())

arr_n = numpy.array([input().split() for i in range(N)],int)
arr_m = numpy.array([input().split() for j in range(M)],int)

concatenate = numpy.concatenate((arr_n,arr_m),axis = 0)
print(concatenate)


