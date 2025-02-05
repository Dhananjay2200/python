# a=int(input("enter the any value between 5 and 9\n"))
try:
    a=input("enter the any value between 5 and 9\n")
    if a=='quit':
        print("you are quit")

    else :
        b=int(a)
        print(b)

except:
    raise ValueError