def format_board(board):
    first_row = ' '
    for i in range(len(board)):
        first_row += str(i + 1)
    joined_rows = [first_row]
    for i in range(len(board)):
        joined_row = str(i + 1) + ''.join(board[i])
        joined_rows.append(joined_row)
    return "\n".join(joined_rows)

def play_game():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]
    print(format_board(board))
    print('\nX to play:\n')
    play_move(board, 'X')
    print(format_board(board))
    print('\nO to play:\n')
    play_move(board, 'O')
    print(format_board(board))

def play_move(board, player):
    row = int(input())
    col = int(input())
    board[row-1][col-1] = player

play_game()


def make_board(size):
    
    
    board = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(' ')
        board.append(row)
    return board

def test():
    board = make_board(3)
    assert_equal(board, [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ])
    board[0][0] = 'X'
    assert_equal(board, [
        ['X', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ])

test()


