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
        print("Key %s Value %s " % (k, v))

func2(a="1", b="2", c=3)

# document/doc string in function
def someFun():
    """Example of document string"""

print(someFun.__doc__)

# Function is pass by reference
def func3(list):
    list[0] = 10

list = [1, 2, 3, 4]
func3(list)
print(list)

def swap(x, y):
    temp = x
    x = y
    y = temp
    print("Inside swap function-> After swapping => x= %s , y= %s " % (x, y))

x, y = 1, 2
print("Before swapping => x= %s , y= %s " % (x, y))
swap(x, y)
print("Outside swap function-> After swapping => x= %s , y= %s " % (x, y))

# Anonymous / lambda function
string = lambda s: print(s)
string("Lambda example")

tables = [lambda x=x: x * 10 for x in range(1, 11)]
print("total lamdas ", len(tables))
for table in tables:
    print(table())
