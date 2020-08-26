'''
August 25, 2020
Sudoku Solver using Backtracking Algorithm
Angela Zhang

backtracking algorithm logic
1. pick an empty box
2. try all numbers
3. find one that works
4. repeat
5. as soon as solution cannot be completed, backtrack
    - erase current, go back to previous one and try others
    - if not, keep going back and try others until it does
'''

# empty slots denoted by 0
board = [

    # valid board
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]

    # invalid board
    # [7,8,0,4,0,0,1,2,0],
    # [6,0,0,0,7,5,0,0,9],
    # [0,0,0,6,0,1,0,7,8],
    # [0,0,7,0,4,0,2,6,0],
    # [0,8,1,0,5,0,9,3,0],
    # [9,0,4,0,6,0,0,0,5],
    # [0,7,0,3,0,0,0,1,2],
    # [1,2,0,0,0,7,4,0,0],
    # [0,4,9,2,0,6,0,0,7]

]

def solve_board(b):
    # base case
    found = find_empty(b)
    if not found:
        return True # board is solved

    row = found[0]
    col = found[1]

    for i in range(1, 10): # tries numbers 1-9
        if is_valid(b, i, found):
            b[row][col] = i # update board if valid number

            if solve_board(b): # recursive calls solve_board() on new board
                return True

            b[row][col] = 0 # backtrack if not viable

    return False # cannot solve


def print_board(b): # prints out board for visualization
    n = len(b) # dimension of board

    for row in range(n):
        print_row = "|  "  # row to be printed, reset every row
        if row % 3 == 0 and row != 0:
            print("-------------------------------------")
        for column in range(n):
            print_row += (str(b[row][column]) + "  ")
            if (column + 1) % 3 == 0:
                print_row += "|  "
        print(print_row)

def is_valid(b, value, pos):
    n = len(b)  # dimension of board
    r = pos[0] # row ind of value
    c = pos[1] # column ind of value

    # check row
    for i in range(n):
        if b[r][i] == value and i != c:
            return False

    # check column
    for i in range(n):
        if b[i][c] == value and i != r:
            return False

    # check 3 x 3
    box_x = c // 3
    box_y = r // 3 # gives us x,y coordinates of 3x3 box of value
    for row in range(box_y*3, box_y*3 + 3):
        for column in range(box_x*3, box_x*3 + 3):
            if b[row][column] == value and (row, column) != pos:
                return False

    return True


def find_empty(b): # helper function that returns tuple with coordinates of empty slot, false if no empty
    n = len(b)  # dimension of board

    for row in range(n):
        for column in range(n):
            if b[row][column] == 0:
                return (row, column)

    return False


print("original board:")
print_board(board)
solve_board(board)
print("\n" + "solution:")
if not find_empty(board):
    print_board(board)
else:
    print("invalid board. unable to solve")