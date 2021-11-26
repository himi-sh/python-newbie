# 1. IDENTITY OPERAOR is and not is
x = 10
y = 20

if (x is 10):
    print("x is 10")
if (x is not y):
    print("x is not y")


# 2. MEMBERSHIP OPERATOR in and not in

b = [5, 7, 10, 20]

if (10 in b):
    print("10 in b")
if (11 not in b):
    print("11 not in b")

# 3. TERNARY OPERATOR in python

a = 5 if 1 < 2 else 2
print("value of a is ", a)

c, d = 11, 20
print((c, d) [c < d]) # c is at index 0, d at 1, if c < d true then index 1 will get printed
print({True: c, False: d} [c < d])
print((lambda: d, lambda: c)[c < d]())

print("1st ternary part 1" if 1 != 1 else "1st ternary part 2" if 2 == 2 else "2nd ternary part 2")

# ANY, ALL
print(any([True, False]))
print(all([True, False]))

# checking even odd
list = []
for i in range(1,11):
    list.append(i%2==0)
print("list=", list, " ", any(list))
print(all(list))
