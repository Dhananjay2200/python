class myclass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"value is {self._value}")
    
    @property # this is a getter
    def ten_value(self):
        return self._value
    @ten_value.setter
    def ten_value(self,newvalue):
        self._value=newvalue/10

obj=myclass(10)
obj.ten_value=1000
print(obj.ten_value)
obj.show()