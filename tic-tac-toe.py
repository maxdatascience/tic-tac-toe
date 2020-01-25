import random


def display_board(board):
    print('\n'*100)
    print(f"| {board[7]} | {board[8]} | {board[9]} |")
    print("-------------")
    print(f"| {board[4]} | {board[5]} | {board[6]} |")
    print("-------------")
    print(f"| {board[1]} | {board[2]} | {board[3]} |")

def player_input():
    """
    OUTPUT  = (Player 1  marker, Player 2 marker)
    """
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player1: Choose X or O: ').upper()
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def win_sequence(list, marker):
    return list == marker

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    marker = [mark]*3
    # check horizontal lines
    for line_index in range(1, 10, 3):
        win_list = board[line_index:line_index+3]
        if win_sequence(win_list, marker):
            return True
    # check vertical lines
    for line_index in range(1,4):
        win_list = board[line_index:line_index+7:3]
        if win_sequence(win_list, marker):
            return True
    # check diagonals
    win_list = board[1:10:4]
    if win_sequence(win_list, marker):
        return True
    win_list = board[3:8:2]
    if win_sequence(win_list, marker):
        return True
    return False

def choose_first():
    # 0 - player 1 goes first, 1 - player 2 goes first
    return random.randint(0,1)

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return (board.count('X') + board.count('O')) == 9

def player_choice(board):
    position = None
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position (1-9)'))
    return position

def replay():
    replay = input("Play again? (Y)").upper()
    return replay == 'Y'

if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')

    while True:
        # Set up the game
        board = ['#'] + [' ']*9
        # Player 1 choose either X or O
        players = player_input()
        # Who's turn first
        turn = choose_first()  # 0 player 1   1 player 2
        print(f"Player {turn+1} goes first")
        play_game = input('Ready to play (Y)? ').upper()
        if play_game == 'Y':
            game_on = True
        else:
            game_on = False
        while game_on:
            display_board(board)
            for i in range (turn,2):
                print(f"Your turn Player {i+1}")
                position = player_choice(board)
                if space_check(board, position):
                    place_marker(board, players[i], position)
                display_board(board)
                if win_check(board, players[i]):
                    if i:
                        print(f"Congratulations Player 2")
                    else:
                        print(f"Congratulations Player 1")
                    break
            turn = 0
            if full_board_check(board) or win_check(board, 'X') or win_check(board, 'O') :
                break
        if not replay():
            break