####try/exception use cases####

#try to execute the code inside the try statement
try:
    n1 = int(input("int 1: "))
    n2 = int(input("int 2: "))
    print(n1/n2)
#if it doesnt work, it enters the except statement and prints the error description
except TypeError as e:
    print(e)
#in case the try statement is succesful, the else block is executed
else:
    print("All good.")


####isinstance use cases####

n3 = int(input("Type a number."))
if isinstance(n3, int):
    print("Integer")
else:
    print("Not integer")