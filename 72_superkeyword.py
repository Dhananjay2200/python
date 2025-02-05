class Employee:#superclass
    def __init__(self,name,id):
        self.name= name
        self.id=id


class programmer(Employee): #subclass
    def __init__(self,name,id,lang):
        super().__init__( name,id)   # this super means go to backwork and fetch the data from parent class Employee method init
        self.lang = lang

Dk=programmer("Dhananjay","2345","python")

print(Dk.name)
print(Dk.id)
print(Dk.lang)

 
