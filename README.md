# Sudoku Solver

## Outline

A program that makes use of a brute force backtracking algorithm to solve 9x9 Sudoku puzzles, finding the solution in a matter of seconds. A modular approach was taken to improve maintainability and readibility of code and a total of four specialised functions are used to produce an overall solution.

## Structure

The following functions are used:

### _isComplete_
checks if the puzzle is complete and returns this as a Boolean.
### _isValid_
checks if the current puzzle state is valid and returns this as a Boolean.
### _duplicatesExist_
takes a list and checks for duplicates, returning this as a Boolean.
### _showGrid_
prints out a grid to the console.

