st=input("Enter your message")
words=st.split(" ")
coding=input("1 for coding or 0 for decoding")
coding=True if(coding=="1")else False
if(coding):
    nwords=[]
    for word in words:
    # print(word)
        if(len(word)>=3):
            r1='edf'
            r2='dcd'
            stnew=r1+word[1:]+word[0]+r2

            nwords.append(stnew)
        else:
            nwords.append(word[::-1])  # it means the string is not 3 char so string reverse automatically
    print(' '.join(nwords)) 
    

else:
    nwords=[]
    for word in words:
        if(len(word)>=3):
            stnew=word[3:-3] # remove the all random charater
            stnew=stnew[-1]+stnew[:-1] # it means the last char + without last char string
            nwords.append(stnew)
        else:
            nwords.append(word[::-1]) 
    print(' '.join(nwords))