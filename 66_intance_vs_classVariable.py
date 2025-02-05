class Employee:
    companyname="Apple" #this is a class variable
    noOfemployee=0  #this is a class variable
    def __init__(self,name):
        self.name=name #this is a intance variable
        self.raise_amount = 0.2  #this is a intance variable
        Employee.noOfemployee += 1
    def showDetails(self):
        print(f"the name of employee is {self.name} and the raise amount in {self.noOfemployee} sized {self.companyname} is {self.raise_amount} ")

emp1= Employee("harry")
emp1.showDetails()
emp1.companyname="Apple India" # that way we can change class variable only for emp1
# Employee.companyname="Apple India" # This way we can change class variable for entire class

emp1.showDetails()
emp2= Employee("Dhananjay")
emp2.companyname="Google"
emp2.showDetails()
