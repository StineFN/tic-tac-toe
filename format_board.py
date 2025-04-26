def format_board(board):
    joined_rows = []
    divider = "\n   -"
    cols = "   "
    
    for i in range(len(board)):
        cols += str(i+1) + " "
        board[i].insert(0,str(i+1) + " ")
    joined_rows.append(cols.rstrip())
    
    for row in board:
        joined_rows.append("|".join(row))
   
    for _ in range(len(board)-1):
        divider += "+-"
    divider += "\n"
    
    string = divider.join(joined_rows)
    return string
