
#you can write into a file using the write function using "w"
#you can append to an existing file by using "a", reruning, the program keeps on appending same line to the end
#so using "w" a file can be overwritten but if you change the mode to append, it adds on file
#depending on what you wanna use, edit the second argument
text = "This file was created using open from inside vscode"
with open('myOtherfile.txt', 'w') as file:
    file.write(text)