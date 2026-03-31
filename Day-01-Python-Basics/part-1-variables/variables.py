# DAY 01 — VARIABLES

# 1. Basic Variables

name = "Alice"
age = 25
print(name, type(name))
print(age, type(age))

# 2. Reference Behavior

a = [1, 2, 3]
b = a
b.append(4)
print(a)  # changed

# 3. Reassignment

x = 10
x = 20

# 4. Dynamic Typing

var = 10
var = "hello"
var = [1, 2]

# 5. Integer Interning

a = 256; b = 256
print(a is b)

a = 257; b = 257
print(a is b)

# 6. Swap

x, y = 1, 2
x, y = y, x

# 7. del

temp = 10
del temp

# 8. is vs ==

a = [1,2]
b = [1,2]
print(a == b)
print(a is b)
