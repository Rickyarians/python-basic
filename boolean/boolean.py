# true
print(10 > 9) #true
# false
print(10 == 9) 
# false
print(10 < 9)


a = 200
b = 33
# if state true / false
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


print(bool("Hello"))
print(bool(15))

# values are fale

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

x = "test"
print(isinstance(x, int))

x = 100
print(isinstance(x, int))


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")