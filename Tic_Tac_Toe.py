lst_1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
count = 0
print('Tic Tac Toe Game')
print('Games Rules:')
print('\t 1. Only Two Platers')
print('\t 2. Each have one move')
print('\t 3. Each step player can fill box(places) with thir symbol')
print('\t 4. which player complete stright and cros line of box(places) he is winner')
print('\t 5. Player 1. symbol(X) and player 2. symbol(O)')
print('\t [0 | 1 | 2]')
print('\t [3 | 4 | 5]')
print('\t [6 | 7 | 8]')
play_game = input('Are you ready to play? Enter Yes or No.')

if play_game.lower()[0] == 'y':
    game_on = True
else:
    game_on = False

def print_box():
    print('\t', lst_1[0], '|', lst_1[1], '|', lst_1[2])
    print('\t', lst_1[3], '|', lst_1[4], '|', lst_1[5])
    print('\t', lst_1[6], '|', lst_1[7], '|', lst_1[8])

def get_ply1_mov(num):
    plt1 = num
    lst_1[plt1] = 'X'

def get_ply2_mov(num):
    plt2 = num
    lst_1[plt2] = 'O'

def reset():
    print('reatart.....')
    return 0


def check_result(mark):
    return ((lst_1[6] == mark and lst_1[7] == mark and lst_1[8] == mark) or # across the bottom
    (lst_1[2] == mark and lst_1[3] == mark and lst_1[5] == mark) or # across the middle
    (lst_1[0] == mark and lst_1[1] == mark and lst_1[2] == mark) or # across the top
    (lst_1[8] == mark and lst_1[3] == mark and lst_1[0] == mark) or # down the middle
    (lst_1[7] == mark and lst_1[4] == mark and lst_1[1] == mark) or # down the middle
    (lst_1[8] == mark and lst_1[5] == mark and lst_1[2] == mark) or # down the right side
    (lst_1[6] == mark and lst_1[4] == mark and lst_1[2] == mark) or # diagonal
    (lst_1[8] == mark and lst_1[4] == mark and lst_1[0] == mark)) # diagonal

while game_on:
    #print(count)
    if count == 9:
        print("No Possible Steps Game Draw")
        game_on = False
        break

    if (count % 2) == 0:
        plt1 = int(input("Enter position X :"))
        if lst_1[plt1] == 'X' and 'O' and plt1 > 8:
            print('Box is already filled / input invalid')
            print_box()
        else:
            get_ply1_mov(plt1)
            print_box()
            count += 1
            if check_result('X') == True:
                print('Player 1 - X is Win')
                opt = input('Do you want to play again? Enter Yes(y) or No(n):')
                if opt.lower()[0] == 'y':
                    game_on = True
                    count = reset()
                else:
                    game_on = False

    else:
        plt2 = int(input("Enter position 0 :"))
        if lst_1[plt2] == 'X' and 'O' and plt2 > 8:
            print('Box is already filled / input invalid')
            print_box()
        else:
            get_ply2_mov(plt2)
            print_box()
            count += 1
            if check_result('O') == True:
                print('Player 2 - O is Win')
                opt = input('Do you want to play again? Enter Yes(y) or No(n):')
                if opt.lower()[0] == 'y':
                    game_on = True
                    count = reset()
                else:
                    game_on = False