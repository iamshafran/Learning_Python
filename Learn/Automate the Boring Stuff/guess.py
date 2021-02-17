# This is a guess the number game.
import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20. You have 6 guesses.')
secretNumber = random.randint(1, 20)

for guessesTaken in range (1, 7):
    print('Take a guess.')
    try:
        guess = int(input())

        if guess < secretNumber:
            print('Your guess is too low. You have ' + str(6 - guessesTaken) + ' guesses left.')
        elif guess > secretNumber:
            print('Your guess is too high. You have ' + str(6 - guessesTaken) + ' guesses left.')
        else:
            break # This condition is for the correct guess!
    except ValueError:
        print('You did not enter a number! You have ' + str(6 - guessesTaken) + ' guesses left.')

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))