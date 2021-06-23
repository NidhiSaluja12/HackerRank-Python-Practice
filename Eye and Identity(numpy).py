import numpy
N,M = list(map(int, input().split()))
numpy.set_printoptions(sign=' ')
identity = numpy.eye(N,M)

print(identity)


