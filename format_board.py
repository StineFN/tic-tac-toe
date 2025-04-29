
def format_board(board):
    size = len(board)
    first_row = '  '
    divider = "\n  -"

    # Create the divier line in the right size
    for _ in range(size-1):
        divider += "+-"
    divider += "\n"

    # Create the first row
    for i in range(size):
        first_row += str(i + 1) + ' '

    joined_rows = [first_row.rstrip()]

    for i in range(size):
        joined_row = str(i + 1) + ' ' + '|'.join(board[i])
        joined_rows.append(joined_row)
    return divider.join(joined_rows)


"""def format_board(board):
    size = len(board)
    line = f'\n  {"+".join("-" * size)}\n'
    rows = [f'{i + 1} {"|".join(row)}' for i, row in enumerate(board)]
    return f'  {" ".join(str(i + 1) for i in range(size))}\n{line.join(rows)}'
    """