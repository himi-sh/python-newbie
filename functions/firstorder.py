# functions are treated as objects in Python

# functions can passed to a variable, passed as an argument or returned from a function

# 1. As an object

def upCase(string):
    return string.upper()

obj = upCase
print("function directly ", upCase("Himani"))
print("using object ", obj("Himani"))

# 2. As an argument

def lowCase(string):
    return string.lower()

def func1(funArg):
    obj = funArg("""Hey, there""")
    print(obj)
func1(lowCase)
func1(upCase)

# 3. As a return type

def adder(x):
    def addMe(y):
        print("addMe is called x=", x)
        return x + y
    return addMe

add15 = adder(15)
add10 = adder(10)

print("15 is added to 1 = ", add15(1))
print("10 is added to 1 = ", add10(1))



