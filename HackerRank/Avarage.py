def average(array):
    array=[int(x) for x in input().split()]
    array=set(array())
    return sum(array)/len(array)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
