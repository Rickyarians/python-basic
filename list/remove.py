# remove by value
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# remove by index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# remove last
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# del by index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# clear
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)