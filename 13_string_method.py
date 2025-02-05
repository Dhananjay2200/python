# String are immutable
a="!!!!! Dhananjay !!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("y!")) #remove the chacter from end 
print(a.replace("Dhananjay","son goku"))
print(a.split(" ")) #after spaceing it is make the list 

blogheading = "intrduction tO jS"
print(blogheading.capitalize())

str1="Welcome to the console!!!"
print(len(str1))
print(len(str1.center(50))) #after the this syntex it will give 25 char space give automatically

print(str1.center(50))
print(a.count("Dhananjay"))
print(a.count("!"))

str1= "Welcome to the console !!!"
print(str1.endswith("!!!"))
print(str1.endswith("to",4,10)) #check the value in between the string by providing start and end index position.

str1="he`s name is dan. he is an honest man."
print(str1.find("is")) # it give the address in the index after this condition is false after it give the -1
print(str1.find("ishhh")) # it give the address in the index after this condition is false after it give the -1
# print(str1.index("ishh ")) #if this condition is false after it give the error

str1="WelcomeToTheConsole"
print(str1.isalnum()) # it check the alphanumeric 

str1="welcome"
print(str1.isalpha()) # it check only alphabet

str1="hello world"
print(str1.islower()) #it is check the the string is in lower or not

str1="joy boy has been return"
print(str1.isprintable())# it is string printabe or not and write the \n this not printable
str1="    "
print(str1.isspace()) #it is decetact the space
str1="World Health Organization "
print(str1.istitle()) # after the spacing check first chacter is capital or not

str1="Python is interpeter language"
print(str1.startswith("python"))
print(str1.swapcase())  # this covert the lower into upper or upper in lower

