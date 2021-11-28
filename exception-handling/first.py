# Exception class hierrachy
# https://docs.python.org/2/library/exceptions.html#exception-hierarchy

# 1. Eg 1

def funct1(a, b):
    try:
        return a / b
    except:
        print("Exception occurred")
    finally:
        print("Exceution done - finally")

print("1st =>",funct1(1,2))
print("2nd =>", funct1(1,0))

