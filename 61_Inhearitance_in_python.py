class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showdetails(self):
        print(f"The name of employee: {self.id} is {self.name}")


class programmer(employee): # this is for rename the class name or and also employee`s all function are also excuted in this function that employee class for that language function is not excuteable for that employee class
    def showlanguage(self):
        print("The default language is python")

e1=employee("rohan",400)
e1.showdetails()
e2=programmer("harry",420)
e2.showdetails()
e2.showlanguage()
