# 3 loops in python: while, for in,

# 1. while
i = 0
while (i < 5):
    i += 1
    print(i)

    # while (i == 5): print("infinite loop")
while (i < 2):
    i += 1
    print(i)
else:
    print("while loop ended")

# 2. for
# iterates over any iteratable object
print("for => list")
for i in ["a", "b", "c"]:
    print(i)

print("for => tuple")
for i in (1, 2, 3):
    print(i)

print("for => dictionary")
dict = {'a': 1, 'b': 2 }
for i in dict:
    print("Dictionary values for key ", i, " value ", dict[i])

    # index
list = [1,2,3]
for i in range(len(list)):
    print(list[i])

# what happens internally of loop
# iter(), next(), StopIteration

list = ['a', 'b', 'c']
it = iter(list)
while True:
    try:
        val = next(it)
        print(val)
    except StopIteration:
        print("Stop iteration is raised")
        break

# Other
# enumerate
for key, value in enumerate(['a','b','c']):
    print("key-", key, " value-", value)

# zip => to combine identical type eg: list-list, dict-dict
# iteritem => iterate dictionary as k, v
# item() => similar to iteriem but is time consuming and not memory efficient
# sorted
# reversed
# range => return list eg range(3) means 0 to 2







