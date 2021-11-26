# Function in Python

def someFunction(someParam):
    print("Some Value ", someParam)
someFunction("Yeah")


# Variable Length Arguments => *non-keyword and **keyword arguments
def func1(*arguments):
    for i in arguments:
        print("Argument -> ", i)
func1(1, 2, 3)
func1([1, 2, 3])

def func2(**args):
    for k, v in args.items():
        print("Key %s Value %s " %(k, v))
func2(a="1",b="2",c=3)





