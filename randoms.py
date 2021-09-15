import random

#gen a random number and float from 1-6 like we rolling a dice
x = random.randint(1,6)
y = random.randint(1,6)
print(x)
print(y)

#we cam also generate a random choice 
#playing rock paper scissors
myList = ['rock','paper','c']
z = random.choice(myList)

#working with a deck of cards ie) Crazy 8
cards = ['1','2','3','4','5','6','7','8','9','J','K','Q','A']
random.shuffle(cards)
print(cards)