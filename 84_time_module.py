import time


# def usingWhile():
#     i = 0
#     while i<500:
#         i = i+1
#         print(i)

# def usingFor():
#     for i in range(500):
#         print(i)

# init = time.time() 
# usingWhile()
# t1 = time.time()-init
# init = time.time() 
# usingFor()
# print(time.time()-init)
# print(t1)

# print(4)
# time.sleep(3) # this function means after 4 printing programm will wait 3 second and after code will run
# print("This is printed after the 3 seconds")

t = time.localtime()
f_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(f_time)

# time.time() module give the current time as a floating-point number,and time in second when time module was initialized the return value is based on computer`s system clock