# text-type
# str

string = "Hello World" 
print(string)
print(type(string))

# numeric type
# int, float, complex
# complex - bilangan imajiner

integer = 10
float_type = 10.5
complex_type = 1j

print(integer)
print(float_type)
print(complex_type)
print(type(integer))
print(type(float_type))
print(type(complex_type))

# sequence types
# list, tuple, range

# tuple tidak dapat dirubah
# tuple berbagai macam tipe data bisa
# tuple kosong ()
# tuple 1 nilai (50,) tetap ada koma
# bisa punya data yang sama

tup1 = ('kimia', 'fisika', 1993, 2017)

tup2 = (1, 2, 3, 4, 5 )
tup3 = (1)

print(tup1)
print(tup1[0:])
print(tup1[0:2])
print(tup1[:4])
print(tup2)
print(tup3)
print(tup2[0])
print(tup1[2])
print(type(tup1))
print(type(tup2))

# range(batas bawah, batas atas, interval)
ranger = range(10)
ranger1 = range(0, 10, 3)
print(ranger)
print(list(ranger))
print(list(ranger1))

# list
# list bisa diubah
list_data = ["satu", "dua"]
print(list_data)
print(type(list_data))
list_data[0] = "tiga"
print(list_data)
# tup1[0] = "test"
# print(tup1)

# mapping type
# dict
xdict = {"name" : "John", "age" : 36}
print(xdict)
print(type(xdict))
print(xdict["name"])

# set types
# set, frozenset
# mengetahui elemen penyusun
# fronze immutable, set tidak

y = set("kocak")
print(y)
y.add('test')
print(y)


# Boolean
true_data = True
false_data = False
print(true_data)
print(false_data)
print(type(true_data))
print(type(false_data))

none_data = None
print(none_data)
print(type(none_data))