from format_board import format_board
from winning_state import winner

def make_board(size):
    board = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(' ')
        board.append(row)
    return board

def print_winner(player):
    print(f'{player} wins!')

def print_draw():
    print("It's a draw!")
def play_move(board, player):
    print(f'{player} to play:')
    row = int(input()) - 1
    col = int(input()) - 1
    board[row][col] = player
    print(format_board(board))

def play_game(board_size, player1, player2):
    board = make_board(board_size)
    max_turns = board_size * board_size
    print(format_board(board))
    
    next_turn = player1
    
    for turn in range(max_turns):
        play_move(board, next_turn)
            
        if winner(board):
            print_winner(next_turn)
            break
            
        if next_turn == player1:
            next_turn = player2
        else:
            next_turn = player1
        
        if turn+1 == max_turns:
            print_draw()    
