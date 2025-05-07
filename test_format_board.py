from format_board import format_board, make_board

board = make_board(3)

def test_make_board():
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

def test_format_board():
    board = [
        ['X', ' ', 'O'],
        ['X', 'X', 'X'],
        ['O', ' ', 'O']
    ]

    board1 = [
        ['X', ' ', 'O', 'X'],
        ['X', 'X', 'X', 'O'],
        ['X', 'X', 'O', 'O'],
        ['O', ' ', 'O', ' ']
    ]

    result = format_board(board)
    assert result == "  1 2 3\n  -+-+-\n1 X| |O\n  -+-+-\n2 X|X|X\n  -+-+-\n3 O| |O"

    result1 = format_board(board1)
    assert result1 == "  1 2 3 4\n  -+-+-+-\n1 X| |O|X\n  -+-+-+-\n2 X|X|X|O\n  -+-+-+-\n3 X|X|O|O\n  -+-+-+-\n4 O| |O| "
    