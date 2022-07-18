#this is the guess the number game
import random
secretnumber = random.randint(1,20)
print('I am thinking of a number 1 to 20')
#ask the player to guess 6 times
for guesstaken in range (1,7):
    print('take a guess')
    guess = int(input())
    if guess < secretnumber :
        print('your guess is too low')
    elif guess > secretnumber :
        print('you are too high')
    else :
        break  # this condition is equal
if guess == secretnumber :
    print('you are correct')
else :
    print('you are not right')