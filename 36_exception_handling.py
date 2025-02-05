# a=input("enter the number:")
# print(f"Muliplication table of {a} is:")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")

# except :
#     print("invalid Input!")


# # that up side code means if any error throw then it give a message and program at not end not yet and running program after that code

# print("some imp lines of code")
# print("end of program")

try:
    num = int(input("enter an integer :"))
    a=[6,3]
    print(num)
    print(a[num])
# except Exception as e:   # it give the compiler error 
#     print(e)
except ValueError:
    print("this is not integer")

except IndexError:
     print("Index error")