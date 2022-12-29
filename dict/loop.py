dictio = {
    "brand" : "Honda",
    "color" : "Black",
    "type" : "Sport",
    "year" : 2001
}

for x in dictio:
    print(x)

# value

for x in dictio.values():
    print(x)

# keys
for x in dictio.keys():
    print(x)

for x,y in dictio.items():
    print(f"{x} = {y}")