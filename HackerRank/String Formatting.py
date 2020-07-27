import decimal
A=int(input())
for i in range(A):
    print("{} {} {} {}".format(decimal.Decimal(i),oct(i),hex(i).upper(),bin(i)))
