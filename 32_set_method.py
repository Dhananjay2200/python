cities={"tokyo","madrid","berlin","delhi"}
cities2= {"tokyo","seoul","kabul","madrid"}
# c=cities.union(cities2) # all element save in new set c
# print(c)
# cities.update(cities2)
# print(cities) # update the element cities from cities2
# c=cities.intersection(cities2)  # giving a new set
# cities.intersection_update(cities2) #update in existing set from anther set
# cities.symmetric_difference_update(cities2) # not similar element are print
# c=cities.difference(cities2) # print the simalar element in new set
# cities={"tokyo","berlin","delhi"}
# cities2= {"seoul","kabul","madrid"}

# print(cities.isdisjoint(cities2)) # it check the no one element is same in both set

cities={"tokyo","madrid","berlin","delhi"}
cities2= {"tokyo","madrid"}
# print(cities.issuperset(cities2)) # it is called that cities2 all element are present in cities
# print(cities2.issubset(cities)) # cities2 whole set is fill in cities set
# cities.remove("tokyo") # this element is not present in set then throw error
# cities.discard("tokyo") # this not throw error element is not present in set
# item=cities.pop() # this method pop any random element from set
# print(item)
# del cities # it is delete the intire set 
# cities.clear() #clear the all element from the set
print(cities)




