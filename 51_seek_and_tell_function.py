# with open ('file.txt','r') as f:
#     #move the 10th byte in the file
#     f.seek(10) 
#     #read the next 5 byte 
#     data=f.read(5)
#     print(data)

with open ('file.txt','r') as f:
    #read the first 10 charter in f
    f.read(10)
    #save the current location
    current_location=f.tell() 
    print(current_location)

    #seek to the current location 
    f.seek(current_location)
    print(current_location)
