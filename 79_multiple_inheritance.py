class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Dancer,Employee): # after the using of mro method when we write first place class then that class data will excuted in output l 
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name

o  = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show() 
print(DancerEmployee.mro())


# MRO stands for Method Resolution Order. It is an algorithm used by Python to determine the order in which methods are searched for in a class hierarchy. This is especially important in Python because it supports multiple inheritance, meaning that a class can inherit from multiple parent classes.