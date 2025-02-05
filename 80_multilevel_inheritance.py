class animal: # this a main class
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def showDetails(self):
        print(f"name is {self.name}")
        print(f"species is {self.species}")

class dog(animal):  #This dog class take the data from animal class
    def __init__(self,name,breed):
        animal.__init__(self,name,species="dog")
        self.breed = breed

    def showDetails(self):
        animal.showDetails(self)
        print(f"breed is {self.breed}")

class goldenRetriver(dog):  # this class take the data from dog class
    def __init__(self,name,color):
        dog.__init__(self,name,breed="golden retriver")
        self.color = color

    def showDetails(self):
        dog.showDetails(self)
        print(f"The color is {self.color}")

o = goldenRetriver("tony","white")
o.showDetails()
print(goldenRetriver.mro())
