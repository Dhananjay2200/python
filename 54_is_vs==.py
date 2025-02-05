a=3
b=3
c=[1,2,3]
d=[1,2,3]
e=None
print(a is b) #exact location of object in memory
print(a == b) #value
print(c is d) #exact location of object in memory
# this is false because python will make different location for both list 
print(c == d) #value
print(e is None)

