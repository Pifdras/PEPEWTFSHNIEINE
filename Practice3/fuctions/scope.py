# A variable is only available from inside the region it is created. This is called scope.
# A variable created inside a function belongs to the local scope of that function, 
# and can only be used inside that function.
def myfunc():
  x = 300 # local scope
  print(x)

myfunc()

# As explained in the example above, the variable x is not available outside the function, 
# but it is available for any function inside the function:
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

# If you operate with the same variable name inside and outside of a function, 
# Python will treat them as two separate variables, one available in the global scope (outside the function) 
# and one available in the local scope (inside the function):
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.
def myfunc():
  global x
  x = 300

myfunc()

print(x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

# The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function.
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

# Python follows the LEGB rule when looking up variable names, and searches for them in this order:
#   Local - Inside the current function
#   Enclosing - Inside enclosing functions (from inner to outer)
#   Global - At the top level of the module
#   Built-in - In Python's built-in namespace
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)
