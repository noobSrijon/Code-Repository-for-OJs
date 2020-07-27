"""A=int(input())
X=[int(x) for x in input().split()]
print(sum(set(X))/len(set(X)))
"""
def average(array):
    return sum(set(array))/len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
