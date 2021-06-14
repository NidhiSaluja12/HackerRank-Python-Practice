def average(array):
    set1 = set(array)
    sum1 = sum(set1)
    length = len(set1)
    res = sum1/length
    return res
    
   

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
