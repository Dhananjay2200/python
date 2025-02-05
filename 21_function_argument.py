def avg(a=2,b=3,c=5):
    print("average is ",(a+b+c)/2)


avg(a=4,b=5) # this code say to the that a and b value is taken from this argument and c value is taken from default from function

def average(*number):
    print(type(number))
    sum=0
    for i in number:
        sum = sum+i

    return sum/len(number)

c= average(5,6,7,1)
print(c)