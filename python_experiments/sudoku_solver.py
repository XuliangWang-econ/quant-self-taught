def print_board(board):
    """Print the Sudoku board in a formatted layout."""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def is_valid_placement(board, num, row, col):
    """Check whether placing a number at (row, col) is valid (row, column, and 3x3 box)."""
    # Check row
    for i in range(9):
        if board[row][i] == num and col != i:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num and row != i:
            return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != (row, col):
                return False

    return True

def check_initial_board(board):
    """Pre-check the initial board for conflicts."""
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != 0:
                # Temporarily clear the cell to test for conflicts
                board[i][j] = 0
                if not is_valid_placement(board, num, i, j):
                    board[i][j] = num  # Restore
                    return False
                board[i][j] = num  # Restore
    return True

def solve(board):
    """Backtracking solver."""
    find = find_empty(board)
    if not find:
        return True  # Solved: no empty cells
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid_placement(board, i, row, col):
            board[row][col] = i  # Try placing
            if solve(board):
                return True
            board[row][col] = 0  # Backtrack

    return False

def find_empty(board):
    """Find the next empty cell (0)."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # Return (row, col)
    return None

# --- Main entry point ---
if __name__ == "__main__":
    # 0 represents an empty cell
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    print("Initial board:")
    print_board(board)
    print("\nChecking board validity...")

    if check_initial_board(board):
        print("Board is valid. Solving...\n")
        if solve(board):
            print("Solved successfully:")
            print_board(board)
        else:
            print("Error: The board has no solution.")
    else:
        print("Error: The initial board contains conflicts.")
