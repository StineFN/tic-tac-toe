def row_winner(board):
    
    #Go through all of the rows
    for row in board:
        first = row[0]
        
        #Compare elements of the row and check if it's a space
        for x in row:
            if x.isspace():
                win = False
                break
            
            elif first != x:
                win = False
                break
            
            else:
                win = True
        if win == True:
            return win
    return win        


def column_winner(board):
    
    #Go through all of the rows
    for col in range(len(board)-1):
        first = board[0][col]
        
        if first.isspace():
            win = False
            continue
    
        for row in range(len(board)-1):
            if first != board[row+1][col]:
                win = False
                break
            else:
                win = True
                
        if win == True:
            return win
    
    return win        

def diagonal_winner(board):
    size = len(board)
    top_L = board[0][0]
    top_R = board[0][size-1]
    
    if top_L.isspace() or top_R.isspace():
        return False
    
    #Check top left to bottom right
    for row in range(1, size-1):
        if top_L != board[row][row]:
            win = False
            break
            
        else:
            win = True
            
    if win == True:
        return win   
        
    #Check top right to bottom left
    for row in range(1, size-1):
        if top_R != board[row][size-1-row]:
            win = False
            break
        else:
            win = True
                
    if win == True:
        return win
            
    return win


def winner(board):
    if row_winner(board) or column_winner(board) or diagonal_winner(board):
        return True
    else:
        return False
