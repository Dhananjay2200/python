# class Person:

#   def __init__(self, name, occ):
#     print("Hey I am a person")
#     self.name = name
#     self.occ = occ

#   def info(self):
#     print(f"{self.name} is a {self.occ}")


# a = Person("Harry", "Developer")
# b = Person("Divya", "HR") 
# a.info()
# b.info()
# # print(a.name)
# # a.name = "Divya"
# # a.occ = "HR"
# # a.info()


def greet(fx):
  def mfx(*args, **kwargs):
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

@greet
def hello():
  print("Hello world")

@greet
def add(a, b):
  print(a+b)
  
# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)

