def format_board(board):
    joined_rows = []
    divider = "\n-"
    for row in board:
        joined_rows.append("|".join(row))
    
    for _ in range(len(board)-1):
        divider += "+-"
    divider += "\n"
    
    string = divider.join(joined_rows)
    return string
