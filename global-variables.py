x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


x = "awesome"

def myfunc():
  #  reassign
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Global keyword

x = "awesome"

def myfunc(): 
  global x # refers to variabel di atasnya
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)