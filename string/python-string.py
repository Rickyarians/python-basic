a = "Hello"
print(a)

# multiline

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


#  single quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# string are arrays

a = "Hello World"
print(a[1])

# loop string component
for x in a:
    print(x)
y = set(a)
print(y) 

# cek panjang string
print(len(a))

# check string 
txt = "The best things in life are free!"
print("free" in txt)
name = "Ricky Ariansyah"
print("ariansyah" in name)
print("Ariansyah" in name)

if "Ariansyah" in name:
    print("Benar")
elif "Ricky" in name:
    print("Benar Juga")
else:
    print("salah")

if "Kocak" not in name: 
    print("Ya Tidak Ada")
else:
    print("ada sih")