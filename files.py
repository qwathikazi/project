import os

#basic file detection using python, remember to import file module
#var pathcalled home with the path to my file
path = '/home/wtc/Desktop/practice/myfile.txt'

if os.path.exists(path):
    print("The location exists!")
    if os.path.isfile(path):
        print("That is a file")
elif os.path.isdir(path):
    print("That is a directory")
else: 
    print("That location does not exists!")