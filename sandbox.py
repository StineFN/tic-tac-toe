from format_board import format_board
from play_game import play_game


testboard = [
        ['X', ' ', 'O'],
        ['X', 'X', 'X'],
        ['O', ' ', 'O']
]

#print(repr(format_board(testboard)))

play_game(3, 'A', 'B')