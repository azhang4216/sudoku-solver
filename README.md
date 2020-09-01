# Sudoku Solver

This is a sudoku solver using backtracking algorithm that solves sudoku boards and also determines if board are solvable.

As compared to the brute force method of testing every possible number O(n^(n²)), backtracking runs at to O(n^m), greatly improving efficiency (n = dimension of the board, m = number of blank spaces).

For rules regarding how sudoku works, [click here](https://sudoku.com/how-to-play/sudoku-rules-for-complete-beginners/#:~:text=Sudoku%20is%20played%20on%20a,the%20row%2C%20column%20or%20square.). 

## Initialization & Version Control
This was written using Python 3.6, so 3.6 is preferred, but older versions of Python should work as well.

No external packages involved.

## Running the Code

Run the script, and the original board and solution output should be printed into console, as such:

```
original board:
|  5  3  0  |  0  7  0  |  0  0  0  |  
|  6  0  0  |  1  9  5  |  0  0  0  |  
|  0  9  8  |  0  0  0  |  0  6  0  |  
-------------------------------------
|  8  0  0  |  0  6  0  |  0  0  3  |  
|  4  0  0  |  8  0  3  |  0  0  1  |  
|  7  0  0  |  0  2  0  |  0  0  6  |  
-------------------------------------
|  0  6  0  |  0  0  0  |  2  8  0  |  
|  0  0  0  |  4  1  9  |  0  0  5  |  
|  0  0  0  |  0  8  0  |  0  7  9  |  

solution:
|  5  3  4  |  6  7  8  |  9  1  2  |  
|  6  7  2  |  1  9  5  |  3  4  8  |  
|  1  9  8  |  3  4  2  |  5  6  7  |  
-------------------------------------
|  8  5  9  |  7  6  1  |  4  2  3  |  
|  4  2  6  |  8  5  3  |  7  9  1  |  
|  7  1  3  |  9  2  4  |  8  5  6  |  
-------------------------------------
|  9  6  1  |  5  3  7  |  2  8  4  |  
|  2  8  7  |  4  1  9  |  6  3  5  |  
|  3  4  5  |  2  8  6  |  1  7  9  |  

Process finished with exit code 0
```

You can modify the board, and make your own sudoku board. If the board is unsolvable, it will indicate so in the console:

```
original board:
|  7  8  0  |  4  0  0  |  1  2  0  |  
|  6  0  0  |  0  7  5  |  0  0  9  |  
|  0  0  0  |  6  0  1  |  0  7  8  |  
-------------------------------------
|  0  0  7  |  0  4  0  |  2  6  0  |  
|  0  8  1  |  0  5  0  |  9  3  0  |  
|  9  0  4  |  0  6  0  |  0  0  5  |  
-------------------------------------
|  0  7  0  |  3  0  0  |  0  1  2  |  
|  1  2  0  |  0  0  7  |  4  0  0  |  
|  0  4  9  |  2  0  6  |  0  0  7  |  

solution:
invalid board. unable to solve

Process finished with exit code 0
```

Both of these example boards are provided in the code itself. Uncomment which you desire, or come up with your own using the same list of list format. Make sure that there are only 9 lists of 9 items each within the bigger list, in order for the program to work.

## Acknowledgments
Thanks to [TechWithTim](https://techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/) for inspiring this idea and [GeekforGeeks](https://www.geeksforgeeks.org/backtracking-introduction/) for providing useful information about the backtracking algorithm. Both sources contributed greatly to making this possible.
