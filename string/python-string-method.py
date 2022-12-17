# method string

from os import sep


tupletest = ("Ricky", "Ariansyah", "Achmad")
separator = " "

x = separator.join(tupletest)
print(x)


# translate
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)

y = txt.partition("could")

print(y)