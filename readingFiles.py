
path = '/home/wtc/Desktop/practice/myFileTest.txt'

#say you misspelled the file extension of the file, it will cause an error called fileNotFound error
#
try:
    with open('myFileTest.txt') as file:
        print(file.read())
except FileNotFoundError as a:
    print(a)
    print('Specified file does not exist')

