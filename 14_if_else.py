# if else condition 
num = 18
if(num<0):
    print("number is the negative")
elif(num>0):
    if(num<=10):
        print("number between 1-10")
    elif(num>10 and num<=20):
        print("number between 11-20")
    else:
        print("number is greater than 20")

else :
    print("the number is zero")