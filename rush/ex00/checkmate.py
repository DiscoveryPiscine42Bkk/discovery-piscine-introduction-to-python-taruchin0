def checkmate(board_str):
    board = board_str.split()
    print(board_str.split())
    size = len(board)
    for i in board:
        if len(i) != size:
            print("Error")
            return
        
    # Find K position
    king_count = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                    king_pos = (i, j)
                    king_count += 1
    if not king_pos:
        print("Error")
        return

    kx, ky = king_pos #int

    def is_valid(x, y):
        return 0 <= x < size and 0 <= y < size #check x y in board or not

    # 1. Pawn: can attack diagonally forward (from bottom to top)
    for dx, dy in [(1, 1), (1, -1)]:
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
