from play_game import make_board
from play_game import print_winner
from play_game import print_draw
from play_game import play_move

player1 = 'S'
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