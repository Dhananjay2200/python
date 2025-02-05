x = 10 # global variable

def my_func():
    global x
    x=5 # this is will change the value of the global variable x
    y=5 # local variable

my_func()
print(x)