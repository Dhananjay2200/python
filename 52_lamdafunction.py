# we make the single function 
def appl(fx,value):
    return 6+fx(value)
double=lambda x: x*2  # in this x is argument and x*2 is return value in the function
cube=lambda x: x*x*x
avg = lambda x,y,z :(x+y+z)/3
print(double(5))
print(cube(5))
print(avg(3,5,10))

print(appl(cube,2))
