import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
coin = ['tails', 'heads']
if coin[toss] == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if coin[toss] == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
