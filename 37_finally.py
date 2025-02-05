def func1():
    try:
        l=[1,5,6,7]
        i=int(input("enter the index number:"))
        print(l[i])
        return 1

    except:
        print("some error occurred")
        return 0
    finally:
        print("I am always excuted")

        # when you in call the function after except nothing code will not exsicuted but for finally keyword compalsary that code will run after the function 

x= func1()
print(x)