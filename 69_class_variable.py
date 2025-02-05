class employee:
    company  = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    
    # this way we change inheritance variable 
    # def change(cls ,newcompany):
    #     cls.company= newcompany
    # This way we can change class variable
    @classmethod
    def change(cls,newcompany):
        cls.company=newcompany

e1=employee()
e1.name="dhananjay"
e1.show()
e1.change("Tesla")
e1.show()
print(employee.company)