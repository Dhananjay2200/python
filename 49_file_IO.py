# READING A FILE 
# f=open('myfile.txt','r') when your file open in txt file simpley you write 'rt' and for binary 'rb' opening the text file is defaultiy set
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE 

f=open('myfile.txt','a')
f.write("Hello world!")
f.close()

# second method of write a file

with open('myfile.txt','a') as f:
    f.write("hey i am inside with")