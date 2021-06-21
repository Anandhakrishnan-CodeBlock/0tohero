from random import random, shuffle

cards = {
    'H-Two': 2, 'H-Three': 3, 'H-Four': 4, 'H-Five': 5, 'H-Six': 6, 'H-Seven': 7, 'H-Eight': 8,
    'H-Nine': 9, 'H-Ten': 10, 'H-Jack': 11, 'H-Queen': 12, 'H-King': 13, 'H-Ace': 14,
    'D-Two': 2, 'D-Three': 3, 'D-Four': 4, 'D-Five': 5, 'D-Six': 6, 'D-Seven': 7, 'D-Eight': 8,
    'D-Nine': 9, 'D-Ten': 10, 'D-Jack': 11, 'D-Queen': 12, 'D-King': 13, 'D-Ace': 14,
    'S-Two': 2, 'S-Three': 3, 'S-Four': 4, 'S-Five': 5, 'S-Six': 6, 'S-Seven': 7, 'S-Eight': 8,
    'S-Nine': 9, 'S-Ten': 10, 'S-Jack': 11, 'S-Queen': 12, 'S-King': 13, 'S-Ace': 14,
    'C-Two': 2, 'C-Three': 3, 'C-Four': 4, 'C-Five': 5, 'C-Six': 6, 'C-Seven': 7, 'C-Eight': 8,
    'C-Nine': 9, 'C-Ten': 10, 'C-Jack': 11, 'C-Queen': 12, 'C-King': 13, 'C-Ace': 14
}
desk = []
item = []
print('War')
print('Games Rules:')
print('\t 1. Cards are shuffled and split into Two Set')
print('\t 2. For Each move comper rank of card in desk')
print('\t 3. If Player 1 have high rank then both move to player 1 card ')
print('\t 4. If Player 2 have high rank then both move to player 2 card ')
print('\t 5. If Player 1 and Player 2 card stored in desk until who get first high rank')
print('\t 6. Steps repeat until one player become empty as Losser')

play_game = input('Are you ready to play? Enter Yes or No.')

if play_game.lower()[0] == 'y':
    game_on = True
else:
    game_on = False

items = list(cards.items())
shuffle(items)
length = len(items)
middle_index = length // 2
ply1 = dict(items[:middle_index])
ply2 = dict(items[middle_index:])


def make_list(value, temp):
    if value == 'play1':
        ply1 = dict(temp)
        print('play1', ply1)
    elif value == 'play2':
        ply2 = dict(temp)
        print('ply2', ply2)
    else:
        war = dict(temp)
        print('desk', war)


def check_card(p_first_value, p_secand_value):
    if p_first_value > p_secand_value:
        print("play 1 have high rank")
        desk = list(ply2)
        result = desk.pop(0)
        size = len(ply1)
        size = size + 1
        temp = list(ply1)
        temp.insert(size, result)
        make_list('play1', temp)

    elif p_first_value < p_secand_value:
        print("play 2 have high rank")
        desk = list(ply1.items())
        result = desk.pop(0)
        size = len(ply2)
        size = size + 1
        temp = list(ply2.items())
        temp.insert(size, result)
        make_list('play2', temp)

    else:
        print("WAR")
        desk = []
        war_ply1 = list(ply1.items())
        temp = war_ply1.pop(0)
        size = len(desk)
        size = size + 1
        desk.insert(size, temp)

        war_ply2 = list(ply2.items())
        temp = war_ply2.pop(0)
        size = len(desk)
        size = size + 1
        desk.insert(size, temp)
        make_list('desk', desk)


while game_on:
    if len(ply1) == 0:
        print("Player 1 is Loosed")
    elif len(ply2) == 0:
        print("Player 2 is Loosed")
    else:
        p1 = ply1.values()
        value_iterator = iter(p1)
        p_first_value = next(value_iterator)

        p2 = ply2.values()
        value_iterator = iter(p2)
        p_secand_value = next(value_iterator)

        check_card(p_first_value, p_secand_value)

