import random

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter \'heads\' or \'tails\':')
    guess = input()

toss = random.randint(0,1)

if toss == 0:
    toss = 'tails'
if toss == 1:
    toss = 'heads'

if toss == guess:
    print('Nice guess!')
else:
    print('Nope! Guess again:')
    guess = input()
    if toss == guess:
        print('Thats it!')
    else:
        print('Nope! You are pretty bad at this game.')