import random

num = random.randint(1,50)

guess = int(input('Guess a number between 1 and 50: '))
guesses = 0
while True:
    if guess < num:
        print('Your guess is too low.')
        guesses += 1
    elif guess > num:
        print('Your guess is too high')
        guesses += 1
    elif guess == num:
        print('Congratulations! Your guess is correct')
        guesses += 1
        break
    guess = int(input('Guess another number: '))

print('You guessed the correct number in ' + str(guesses) + ' guesses.')





