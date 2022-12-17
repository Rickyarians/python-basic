# read the type data module

# type conversion

x = 1
y = 2.8
z = 1j

a = float(x)
print(type(x))
print(type(a))

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)
print(c)
print(type(c))


# create random number
import random
print(random.randrange(1, 10))