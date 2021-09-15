#exception handling - An event detected during 
#execution that interrupts the flow of the programme
#dividing 5 by 0 will cause an exception because 5/0 
#cannot be mathematically done ZeroDivisionError: division by zero
#a very basic way of exception handling is using try
    #anytime you accept user input use a try 
    #1-any time you accept user input would be a good indicator of needing an exception
    #2-code says we will try all of this cod and if an exception happens we will handle it like this

#it is not good practice to let the block rxcept block handle all exceptions so its 
#good to add specific expceptions like 
#using except Exception at the end of the code is good practice so that it
#catches any exceptions you may have skipped by mistake, however, good
#good practice is using specific Exceptions

#ADDITIONAL
#you can call the exception a name and use print so that your 
#programme lets the user know what the exeption is 

#You can also add an ELSE statement at the end of you expt block
#in case you missed any exceptions the else block will handle it
    # the print at the bottom means that the result
    # wil only be printed if no exceptions occur
#finally means that whether on not you catch an exception, the code in the block of code finally will ALWAYS execute 
#finally is a good place to close any files you may have opened

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter the divider: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by Zero! idiot!")
except ValueError as q:
    print(q)
    print("Enter only numbers!")
except Exception as y:  
    print(y)             
    print("Something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")
