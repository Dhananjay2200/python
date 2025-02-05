# for read file line by line
# f=open('myfile.txt','r')

# while True:
#     line=f.readline()   # reads  the single line from file
#     if not line:
#         break
#     print(line)

# for write file line by line 

# f=open('myfile2.txt','w')

# line=['line1\n','line2\n','line3\n','line4\n']
# f.writelines(line)
# f.close()

# for read file line by line
f=open('myfile3.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()   # reads  the single line from file
    if not line:
        break
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])

    print(f"marks of student {i} is maths {m1*2}")
    print(f"marks of student {i} is english {m2*2}")
    print(f"marks of student {i} is sst {m3*2}")
    print(line)