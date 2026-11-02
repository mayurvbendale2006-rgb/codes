
# N-Queens using Backtracking
# First Queen is already placed in the first row

def is_safe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):

    if row == n:
        return True

    for col in range(n):

        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_n_queens(board, row + 1, n):
                return True

            board[row][col] = 0

    return False


# Main Program
n = int(input("Enter number of queens: "))

if n < 1:
    print("Invalid input")

else:
    board = [[0 for i in range(n)] for j in range(n)]

    first_col = int(input("Enter column for first queen (1 to n): "))

    if first_col < 1 or first_col > n:
        print("Invalid column")

    else:
        board[0][first_col - 1] = 1

        if solve_n_queens(board, 1, n):

            print("\nN-Queens Matrix:")

            for row in board:
                for value in row:
                    print(value, end=" ")
                print()

        else:
            print("Solution does not exist for this first queen position")
