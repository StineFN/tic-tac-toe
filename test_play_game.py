from play_game import make_board

board = make_board(3)
assert board == [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]
board[0][0] = 'X'
assert board == [
    ['X', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]