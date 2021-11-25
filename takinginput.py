# Taking single input from User
user = input("Enter user ")
print("User is ", user)
value = input("Enter integer value ")
print("type of ", value, " is ", type(value))

# taking input and typecasting
vInt = int(input("Enter integer "))
print("type of ", vInt, " is ", type(vInt))

# Taking multiple inputs together
# using slit() and list

# 1. Using split method
vList = input("Enter multiple values , separated").split(',')
print(vList)
print(type(vList))
x,y = input("Multiple ints").split()
print("value = ", x, "type = ", type(x))
vCasted1, vCasted2 = list(map(int, input("Enter ints").split()))
print("value = ", vCasted1, "type = ", type(vCasted1))

# 2. Using list
x, y =  [ int(x) for x in input("Enter 2 ints").split() ]
print("value x = ", x, "type = ", type(x))