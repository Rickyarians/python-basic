thistuple = ("apple", "banana", "cherry")
print(thistuple)


# allow duplicate 
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


# length 

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)