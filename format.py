#str.format()= this method gives users more control when displaying output

name ="nandipha"  
surname = "yeko"

print("Hello, my name is {0} and I am {1}\n".format(name,surname))

#you can also use format() to add padding to a string
#you do this by adding colon and the amount of space you want to format
print("Hello, my name is {:15} and I am 22".format(name))           #left
print("Hello, my name is {:>15} and I am 22".format(name))          #right
print("Hello, my name is {:^15} and I am 22".format(name))          #center

#formatting numbers
#we would like to display the first two digits after decimal

number = 3.14159
number2 = 1000
print("\nThe number pi is {:.2f}".format(number))
print("The number pi is {:.3f}".format(number))
print("\nThe number pi is {:,}".format(number2))

#you can display your number in other forms as well - octo, binary, scientific notation etc 
print("\nThe number pi is {:o}".format(number2))
print("The number pi is {:b}".format(number2))
print("The number pi is {:,}".format(number2))
print("The number pi is {:X}".format(number2))
print("The number pi is {:E}".format(number2))

