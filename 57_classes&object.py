class person:
    name="Dhananjay"
    occupation="software developer"
    networth="10"

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person()
b=person()
c=person()
a.name='shubham'
a.occupation = 'Accountant'

b.name="nitika"
b.occupation="HR"



a.info()
b.info()
c.info()