import shutil
import os
        #    (src,dst)
# shutil.copy("dk.py","main.py") #This function copies the file location at src to new location specified by dst.if the destination location already exesist the original file will be overwritten
shutil.copy2("dk.py","main.py") # it is similar like a copy function.but it also preseves meta data
# shutil.copytree("osmodual","python345") # it copy the folder`s data in anothe folder and folder is exsist then data will be overwritten

# shutil.move("exe8.py/file.file","file.file") #we move the file one folder to anther folder
# shutil.move("file.file","exe8.py/file.file")
os.remove("file.file")

