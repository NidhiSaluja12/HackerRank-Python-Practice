import numpy

def arrays(arr):
    a = arr[::-1]
    b = numpy.array(a,float)
    return b
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
