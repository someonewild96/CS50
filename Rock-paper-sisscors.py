print('''Please pick one:
            -> Rock
            -> Scissors
            -> Paper''')

while True:
    game_dict = {'Rock': 1, 'Scissors': 2, 'Paper': 3}
    player_1 = str(input("Player 1: "))
    player_2 = str(input("Player 2: "))
    a = game_dict.get(player_1)
    b = game_dict.get(player_2)
    dif = a - b

    if dif in [-1, 2]:
        print('Congratulations! Player 1 has won!')
        if str(input('Type "Quit" if you want to Quit, press any key to continue\n')) == 'Quit':
            print('game over.')
            break
        else:
            continue
    elif dif in [-2, 1]:
        print('Congratulations! Player 2 has won!')
        if str(input('Type "Quit" if you want to Quit, press any key to continue\n')) == 'Quit':
            print('game over.')
            break
        else:
            continue
    else:
        print('Draw.Please continue.')
        print('')