# class method is a alternative constructor
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

        # simple method
    # def showdetails(self):
    #     print(f"The name of employee is {self.name} and his salary is {self.salary}")

    # classmethod
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0], int(string.split("-")[1]))

e=employee("Dhananjay",1200000)
# e.showdetails()
# simple method
# string ="john-2000000"
# e2=string.split("-")
# print(e2)
e2=employee.fromStr("Dhananjay-2000000")
print(e2.name)
print(e2.salary)

