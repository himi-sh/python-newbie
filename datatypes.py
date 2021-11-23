# Basic Data Type:

# int
vInt = 1
print("checking for int")
print(type(vInt))

# float
vFloat = 2.0
print("checking for float")
print(type(vFloat))

# strings
print("checking for string")
vString = "Hello"
print(type(vString))

# binary
vBinary = bin(1)
print("type is ", type(vBinary))
print("value is ", vBinary)

# boolean
vBoolean = True
print("checking for boolean")
print(type(vBoolean))

# -------------------

# list - mutable, ordered
list = [1, "Himani", 1.2]
print("checking for list")
print(type(list))
print(type([]))

# tuple - immutable, ordered
tuple = (1, "Himani", 1.2, 1)
print("checking for tuple")
print(type(tuple))


# set - mutable, unordered, unique
set = set(tuple)
print("checking for set ")
print(type(set))
print("value is ", set)

# dictionary / map
dict = {1: 'one', 2: 'two', '': 'emtpy', None: 'none', 4.0: 'float', tuple: 'checking tuple as key',
        'val': None}
print("checking for dict")
print(type(dict))
print(type({}))

