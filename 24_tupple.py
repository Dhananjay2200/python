# we can not change the tupple
# it same as like a list
tup=(1,2,76,342,32,"green",True)
print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
if 342 in tup:
    print("yes 342 is present in the tupple")
tup2=tup[1:4]
print(tup2)

tup=(1,)
print(tup)
