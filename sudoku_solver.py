
def solveSudoku(board):
    gridSize = 9
    for row in range(gridSize):
        for col in range(gridSize):
            if board[row][col] == 0:
                for num in range(1, gridSize + 1):
                    if (isValidMove(board, row, col, num)):
                        board[row][col] = num

                        if (solveSudoku(board)):
                            return True  # puzzle solved

                        board[row][col] = 0  # backtrack

                return False  # no valid number found
    return True  # All cells filed


def isValidMove(board, row, col, num):
    gridSize = 9
    # Check row and column for conlicts
    for i in range(gridSize):
        if (board[row][i] == num) or (board[i][col] == num):
            return False  # Conflict found

    # Check the 3x3 subgrid for conflicts
    startRow = (row // 3) * 3
    startCol = (col // 3) * 3

    for i in range(startRow, startRow + 3):
        for j in range(startCol, startCol + 3):
            if (board[i][j] == num):
                return False  # Conflict found

    return True  # no conflicts found


def printTable(board):
    gridSize = 9
    for row in range(0, gridSize):
        if (row == 3) or (row == 6):
            print("---------------------")
        for col in range(0, gridSize):
            if (col == 3) or (col == 6):
                print("|", end=" ")
            print(board[row][col], end=" ")
        print()


sudoku_board = [
    [0, 4, 0, 0, 6, 5, 0, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [6, 0, 0, 9, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 6],
    [2, 3, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 6, 0, 8, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 4, 5],
    [8, 0, 0, 0, 0, 1, 0, 0, 2],
    [0, 1, 0, 5, 0, 0, 0, 9, 3]
]


solveSudoku(sudoku_board)


printTable(sudoku_board)
