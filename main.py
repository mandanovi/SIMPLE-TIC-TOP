print('TIC TAC TOE GAME')
print('Gamer 1 symbol = X')
print('Gamer 2 symbol = O\n\n')
table = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def show_board():
    board = f' {table[0]} | {table[1]} | {table[2]} \n' \
           f'-----------\n' \
           f' {table[3]} | {table[4]} | {table[5]} \n' \
           f'-----------\n' \
           f' {table[6]} | {table[7]} | {table[8]} \n'
    print(board)


show_board()
gamer1 = True
score1 = []
score2 = []
for i in range(9):
    try:
        if gamer1:
            gamer_input = int(input('Gamer 1 (X) select number: ')) - 1
            if gamer_input in score2:
                print(f'\nNumber {gamer_input+1} box has been filled by gamer 2')
            else:
                score1.append(gamer_input)
                table[gamer_input] = 'X'
                show_board()
                gamer1 = False
        else:
            gamer2_input = int(input('Gamer 2 (O) select number: ')) - 1
            if gamer2_input in score1:
                print(f'\nNumber {gamer2_input+1} box has been filled by gamer 1')
            else:
                score2.append(gamer2_input)
                table[gamer2_input] = 'O'
                show_board()
                gamer1 = True
    except ValueError:
        print("\nYou need to input number")
    except IndexError:
        print('\nNumber is a must to be between 1 to 9')

    if table[0] == table[1] == table[2] or table[3] == table[4] == table[5] or table[6] == table[7] == table[8] or \
        table[0] == table[3] == table[6] or table[1] == table[4] == table[7] or table[2] == table[5] == table[8] or \
        table[0] == table[4] == table[8] or table[2] == table[4] == table[6]:
        if gamer1:
            print('GAMER 2(0) WON')
        else:
            print('GAMER 1(X) WON')
        break

    elif i == 8:
        print('TIED GAME, BABY')