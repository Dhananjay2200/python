# letter = "Hey my name is {} and I am from  {}"
letter = "Hey my name is {1} and I am from  {0}"
country= "india"
name="Dhananjay"

# print(letter.format(name,country))
# print(letter.format(country,name))
print(f"Hey my name is {name} and I am from {country}")
print(f"we are use f-string like this : hey my name  is {{name}} and i am from {{country}}")

price=49.099999
txt =f"for only {price:.2f} dollars!"
print(txt)
print(f"{2*30}")