N = 4  
def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()
def is_safe(board, row, col):
    if any(board[row][i] for i in range(col)):
        return False
    if any(board[i][j] for i, j in zip(range(row, -1, -1), range(col, -1, -1))):
        return False
    if any(board[i][j] for i, j in zip(range(row, N), range(col, -1, -1))):
        return False
    return True
def place_queens(board, col):
    if col == N:
        print_board(board)
        return True
    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if place_queens(board, col + 1):
                return True
            board[row][col] = 0  
    return False  
def solve_n_queens():
    board = [[0] * N for _ in range(N)]
    if not place_queens(board, 0):
        print("No solution found.")
solve_n_queens()
