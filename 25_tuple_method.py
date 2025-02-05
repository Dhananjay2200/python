# countries = ("spain","italy","india","england", "germany")
# temp = list(countries)
# temp.append("russia")   # add item
# temp.pop(1)             # remove item
# temp[2]="finland"       # change item
# countries = tuple(temp)
# print(countries)


# tuple indexing
tup1=(0,1,2,3,2,31,1,3,2,3)

# res=tup1.count(3)
# res=tup1.index(3)
res=tup1.index(3,4,8) # it means index syntax as per index(element,start,end)
res =len(tup1)

print(res)