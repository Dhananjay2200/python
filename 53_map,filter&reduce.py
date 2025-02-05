# MAP syntex: map(function,iterable)
# def cube(x):
#     return x*x*x

# print(cube(2))

# l=[1,2,4,6,4,3]
# new=[]
# for item in l:
#     new.append(cube(item))
# print(new)

# upper code shortcut method

# new2=list(map(cube,l))
# # in lamnda function 
# new3=list(map(lambda x: x*x*x,l))
# print(new2)
# print(new3)




# FILTER syntex: filter(predicate,iterable)
l=[1,2,4,6,4,3]
def filter_function(a):
    return a>2

new4=list(filter(filter_function,l)) #in that case which element are not satisfing the they element are not show in output
print(new4)

# # syntex: reduce(function,iterable)
# from functools import reduce
# number = [1,2,3,4,5]
# # calculate the sum of function by reduce function
# def mysum(x,y):
#     return x+y

# sum = reduce(mysum,number)
# print(sum)

# sum process 
# [1,2,3,4,5]
# [3,3,4,5]
# [6,4,5]
# [10,5]
# [15]