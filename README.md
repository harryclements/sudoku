# Sudoku Solver

## Outline

A program that makes use of a brute force backtracking algorithm to solve 9x9 Sudoku puzzles, finding the solution in a matter of seconds. A modular approach was taken to improve maintainability and readibility of code and a total of four specialised functions are used to produce an overall solution.

## Structure

The following functions are used:

### _isComplete_

Checks if the puzzle is complete and returns this as a Boolean.

### _isValid_

Looks at the contents of each row, column anf box in the puzzle and uses the _duplicatesExist_ function to check if the current puzzle state is valid, returning a Boolean.

### _duplicatesExist_

Takes a list as input and checks for duplicate values, returning this as a Boolean.

### _showGrid_

Prints out a given puzzle grid to the console. This functionns prints out the incomplete grid at the beginning and then the completed version at the end. However, it was also useful for the testing process.

