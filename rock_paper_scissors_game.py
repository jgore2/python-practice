import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie!'

    if is_win(user, computer):
        return 'You won :D'

    return 'You lost :('

def is_win(player, opponenet):
    # returns true is player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponenet == 's') \
        or (player == 's' and opponenet == 'p') \
        or (player == 'p' and opponenet == 'r'):
        return True

print(play())