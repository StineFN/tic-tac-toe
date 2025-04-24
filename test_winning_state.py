from winning_state import row_winner 

def test_row_winner():
    board = [
        ['X', ' ', 'O'],
        ['X', 'X', 'X'],
        ['O', ' ', 'O']
    ]

    board1 = [
        ['X', ' ', 'O', 'X'],
        ['X', 'X', 'X', 'O'],
        ['O', ' ', 'O', ' ']
    ]

    result = row_winner(board)
    assert result == True

    result1 = row_winner(board1)
    assert result1 == False
