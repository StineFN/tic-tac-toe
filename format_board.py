def format_board(board):
    joined_rows = []
    divider = "\n   -"
    cols = "   "
    size = len(board)
    
    for i in range(size):
        cols += str(i+1) + " "
        #board[i].insert(0,str(i+1) + " ")
    joined_rows.append(cols.rstrip())
    
    for row in board:
       joined_rows.append("|".join(row))
   
    for _ in range(size-1):
        divider += "+-"
    divider += "\n"
    
    string = divider.join(joined_rows)
    return string

"""
def format_board(board):
    first_row = ' '
    for i in range(len(board)):
        first_row += str(i + 1)
    joined_rows = [first_row]
    for i in range(len(board)):
        joined_row = str(i + 1) + ''.join(board[i])
        joined_rows.append(joined_row)
    return "\n".join(joined_rows)
"""

"""def format_board(board):
    size = len(board)
    line = f'\n  {"+".join("-" * size)}\n'
    rows = [f'{i + 1} {"|".join(row)}' for i, row in enumerate(board)]
    return f'  {" ".join(str(i + 1) for i in range(size))}\n{line.join(rows)}'
    """