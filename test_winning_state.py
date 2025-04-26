from winning_state import row_winner 
from winning_state import column_winner
from winning_state import diagonal_winner
from winning_state import winner

def test_row_winner():
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

    board2 = [
        ['X', ' ', 'O', 'X'],
        ['X', 'O', 'X', 'O'],
        ['X', 'X', 'O', 'O'],
        [' ', ' ', ' ', ' ']
    ]

    result = row_winner(board)
    assert result == True

    result1 = row_winner(board1)
    assert result1 == False

    result2 = row_winner(board2)
    assert result2 == False

def test_column_winner():

    board = [
        ['X', ' ', 'O'],
        ['X', ' ', 'X'],
        ['O', ' ', 'O']
    ]

    board1 = [
        ['X', ' ', 'O', 'X'],
        ['X', 'X', 'O', 'O'],
        ['X', 'X', 'O', 'O'],
        ['O', ' ', 'O', ' ']
    ]

    board2 = [
        ['X', ' ', 'O', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'O', 'O'],
        [' ', ' ', ' ', ' ']
    ]

    result = column_winner(board)
    assert result == False

    result1 = column_winner(board1)
    assert result1 == True

    result2 = column_winner(board2)
    assert result2 == False

def test_diagonal_winner():

    board = [
        ['X', ' ', 'O'],
        ['X', 'O', 'X'],
        ['O', ' ', 'O']
    ]

    board1 = [
        ['X', ' ', 'O', 'X'],
        ['X', 'X', 'O', 'O'],
        ['X', 'X', 'X', 'O'],
        ['O', ' ', 'O', 'X']
    ]

    board2 = [
        ['X', ' ', 'O', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'O', 'O'],
        [' ', ' ', ' ', ' ']
    ]

    result = diagonal_winner(board)
    assert result == True

    result1 = diagonal_winner(board1)
    assert result1 == True

    result2 = diagonal_winner(board2)
    assert result2 == False

def test_winner():

    board = [
        ['X', ' ', 'O'],
        ['X', 'O', 'X'],
        ['O', ' ', 'O']
    ]

    board1 = [
        ['X', ' ', 'O', 'X'],
        ['X', 'X', 'O', 'O'],
        ['X', 'X', 'O', 'O'],
        ['O', ' ', 'O', 'X']
    ]

    board2 = [
        ['X', ' ', 'O', 'X'],
        ['X', 'O', 'X', 'X'],
        ['X', 'X', 'O', 'O'],
        [' ', ' ', ' ', ' ']
    ]

    result = winner(board)
    assert result == True

    result1 = winner(board1)
    assert result1 == True

    result2 = winner(board2)
    assert result2 == False