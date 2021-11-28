# Exception class hierrachy
# https://docs.python.org/2/library/exceptions.html#exception-hierarchy

# 1. Eg 1

def funct1(a, b):
    try:
        d = 1
        return a / b
    except:
        print("Exception occurred")
    finally:
        print("Exceution done - finally")

print("1st =>", funct1(1, 2))
print("2nd =>", funct1(1, 0))

# 2. Eg 2

def AbyB(a, b):
    try:
        c = ((a + b) / (a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print("c = ", c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)


# 3. Specifying Exceptions and raising Exception s
def func2():
    try:
        raise NameError
    except NameError:
        print("raised and handled")

func2()
