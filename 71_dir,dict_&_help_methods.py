class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age
      self.version = 1

# for this dict() attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection.
p = Person("John", 30)
print(p.__dict__)
print(dir(p))

# for help() The help() function is used to get help documentation for an object, including a description of its attributes and methods.
# print(help(Person))

# This dir() return the all methods and atribute avalible for the that object 
x = [1, 2, 3]
print(dir(x))
print("This is a add")
print(dir('__add__'))