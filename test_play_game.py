from play_game import print_winner, print_draw, get_placement


player1 = 'S'
board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]

def test_print_winner(capsys):
    print_winner(player1)
    captured = capsys.readouterr()
    result = captured.out 
    assert result.strip() == "S wins!"


def test_print_draw(capsys):
    print_draw()
    captured = capsys.readouterr()
    result = captured.out 
    assert result.strip() == "It's a draw!"


"""def test_get_placement(monkeypatch):
    inputs = iter([1, 2])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    row, col = get_placement()
    
    assert row == 0
    assert col == 1
"""
"""
def test_play_move(monkeypatch):
    board = make_board(3)
    #captured = capsys.readouterr()
    #result = captured.out 
    inputs = iter([1, 1])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    play_move(board, player1)
    assert board[0][0] == player1
    #assert result.strip() == "S to play:\n  1 2 3\n  -+-+-\n1 S| | \n  -+-+-\n2  | | \n  -+-+-\n3  | | "

    """