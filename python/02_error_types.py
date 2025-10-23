#try/exception use cases

try:
    n1 = int(input("int 1: "))
    n2 = int(input("int 2: "))
    print(n1/n2)
except TypeError as e:
    print(e)


