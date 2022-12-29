thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

print(x)

# get 

y = thisdict.get("model")
print(y)


# get keys
print(thisdict.keys())

# change

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "Year" : 1964
}

x = car.keys()

print(x)

car["color"] = "white"

print(x)

# values

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change




# get Items

print(thisdict.items())

# cek key if exist

if "model" in thisdict:
    print("Test")