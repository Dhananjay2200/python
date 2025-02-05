# in class not a compalsray to pass the self argument in method but also use the static method
class Math:
    def __init__(self,num):
        self.num=num
    def addtonum(self):
        self.num=self.num+1
    @staticmethod
    def add(a,b):
        return a+b

a=Math(5)
print(a.num)
# a.addtonum(6)
print(a.num)

print(Math.add(7,2))


