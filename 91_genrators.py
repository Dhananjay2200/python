# genrators is genrats value one by one
def genrators():
    for i in range(5):
        yield i # this statement is return the value from the genrators and suspend the excicution  until next value is requested

gen = genrators()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
for j in gen:
    print(j)





