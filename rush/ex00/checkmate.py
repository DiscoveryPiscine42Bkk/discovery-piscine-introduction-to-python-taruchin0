def checkmate(board_str):
    board = [list(line) for line in board_str.strip().split('\n')]
    size = len(board)
    
    # Find King's position
    king_pos = None
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Fail")
        return

    kx, ky = king_pos

    def is_valid(x, y):
        return 0 <= x < size and 0 <= y < size

    # Define check for each piece
    # 1. Pawn: can attack diagonally forward (from bottom to top)
    for dx, dy in [(-1, -1), (-1, 1)]:
        x, y = kx + dx, ky + dy
        if is_valid(x, y) and board[x][y] == 'P':
            print("Success")
            return

    # 2. Bishop and Queen diagonals
    for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1)]:
        x, y = kx + dx, ky + dy
        while is_valid(x, y):
            piece = board[x][y]
            if piece != '.':
                if piece in ['B', 'Q']:
                    print("Success")
                    return
                break
            x += dx
            y += dy

    # 3. Rook and Queen in straight lines
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        x, y = kx + dx, ky + dy
        while is_valid(x, y):
            piece = board[x][y]
            if piece != '.':
                if piece in ['R', 'Q']:
                    print("Success")
                    return
                break
            x += dx
            y += dy

    # If no threats found
    print("Fail")
