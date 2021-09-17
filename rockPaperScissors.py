import random

choices = ['rock', 'paper', 'scissors']
option = random.choice(choices)
userInput = None

while userInput not in choices:
    userInput = input("\nRock, Paper or Scissors?\nEnter: ").lower()

if userInput == option:
    print("It's a tie!")
    print("Computer: ",option )
    print("PLayer: ",userInput)

elif userInput == "rock" and (option == "paper" or option == "scissors"):
    print("Computer: ",option)
    print(f"You win! {userInput} beats {option}")

# else if:
#     print('Sorry, try again')
#     userInput = input("\nRock, Paper or Scissors?\nEnter: ").lower()

