def greet(fx):
    def mfx(*args,**kwargs): #*args is take a argument as tupple and **kwargs is take argument as dictonary
        print("Good morning")
        fx(*args,**kwargs)
        print("Thank you for this for function ")
    return mfx
    
@greet
def hello():
    print("hello world")
@greet
def hello():
    print("hello world")

def hello():
    print("hello world")
@greet
def add(a, b):
    print(a+b)

hello()  
greet(hello)()  #second method of greet calling 
add(4,5)