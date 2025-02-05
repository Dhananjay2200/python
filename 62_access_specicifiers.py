# this way we access the publically
# class employee:
#     def __init__(self):
#         self.name="Dhananjay"


# obj=employee()
# print(obj.name)
class employee:
    def __init__(self):
        self.__name="Dhananjay"


obj=employee()
# print(obj.name) we can not access direcatly 
print(obj._employee__name) #we can  access indirecatly 
#this method called name mangling

# name magling in python is technic  used to proceted class privite and subclass privite attibutes from begin accidently

class student:
    def __init__(self):
        self._name="Dhananjay"

    def _funName(self): # protected method
        return "codewithharry"
    
class subject(student): # inherited method
    pass

obj=student()
obj2=subject()

# calling by object of class student class 
print(obj._name)
print(obj._funName())
# calling by object of subclass 
print(obj2._name)
print(obj2._funName())