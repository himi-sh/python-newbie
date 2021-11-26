# example 1 :
def someFunc():
    yield 1
    yield 2

for i in someFunc():
    print(i)

# example 2 : to find cube of numbers
print("Cubes")

def cubeFunc():
    i = 1
    while (True):
        yield i * i * i
        i = i + 1

for j in cubeFunc():
    if (j > 100):
        break
    print(j)
