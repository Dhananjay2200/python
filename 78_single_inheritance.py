class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("sound made by animal")

class dog(Animal):
    def init(self,name,breed):
        Animal.__init__(self,name,species="dog")
        self.breed=breed
    def make_sound(self):
        print("bark!!")

s
d= Animal("vodafone","dog")
d.make_sound() 

d2=dog("Vodafone","dog")
d2.make_sound()