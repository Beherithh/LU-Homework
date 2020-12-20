from random import randint

catalog = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
player, comp = 0, 0

print("Game - \"Rock / Paper / Scissors\"")
while player < 3 and comp < 3:
    print('Enter 1 for Rock, 2 for Paper, 3 for Scissors')
    com_choice = randint(1, 3)

    try:
        pl_choice = int(input('Your turn: '))
        result = pl_choice - com_choice
        print(f"{catalog[pl_choice]} vs {catalog[com_choice]}")
    except:
        print('Wrong input')
        continue

    if result == 0:
        print(f'Draw \n {player}:{comp}\n')
    elif result == 1 or result == -2:
        player += 1
        print(f'User wins this round \n {player}:{comp}\n')
    else:
        comp += 1
        print(f'Computer wins this round \n {player}:{comp}\n')

if player > comp:
    print('User wins!')
else:
    print('Computer wins!')
