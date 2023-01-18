import random
NUMBER = random.randint(1, 100)
while True:
    guess = int(input('Guess a number: '))
    if guess == NUMBER:
        print('You got it!')
        break
    else:
        print('Wrong, try again.')
