import random, sys

print('Rock Paper Scissors')

wins = 0
losses = 0
ties = 0
print('WINS: %s, LOSSES: %s, TIES: %s\n' %(wins, losses, ties))

while True:
    num = random.randint(1, 3)
    playerMove = str(input('Enter your move: (r)ock, (p)aper, (s)cissors, (q)uit: '))
    # computerMove = ''
    if num == 1:
        computerMove = 'ROCK'
    elif num == 2:
        computerMove = 'PAPER'
    else:
        computerMove = 'SCISSORS'

    if playerMove == 'r' and computerMove == 'ROCK':
        print('ROCK versus ROCK')
        print('WOW Its a tie!!')
        ties = ties + 1
    elif playerMove == 'p' and computerMove == 'ROCK':
        print('PAPER versus ROCK')
        print('You win!!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'ROCK':
        print('SCISSORS versus ROCK')
        print('You lose')
        losses = losses + 1
    elif playerMove == 'r' and computerMove == 'PAPER':
        print('ROCK versus PAPER')
        print('You lose')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 'PAPER':
        print('PAPER versus PAPER')
        print('You lose')
        ties = ties + 1
    elif playerMove == 's' and computerMove == 'PAPER':
        print('SCISSORS versus PAPER')
        print('You win!!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'SCISSORS':
        print('SCISSORS versus SCISSORS')
        print('WOW Its a tie!!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 'SCISSORS':
        print('ROCK versus SCISSORS')
        print('You win!!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'SCISSORS':
        print('PAPER versus SCISSORS')
        print('You lose')
        losses = losses + 1
    elif playerMove == 'q':
        print('Bye')
        sys.exit()
    else:
        print('Please enter a valid move.')

    print('WINS: %s, LOSSES: %s, TIES: %s\n' % (wins, losses, ties))
