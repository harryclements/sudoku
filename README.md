# Sudoku Solver

## Outline

A program that makes use of a brute force backtracking algorithm to solve 9x9 Sudoku puzzles, finding the solution in a matter of seconds. A modular approach was taken to improve maintainability and readibility of code and a total of four specialised functions are used to produce an overall solution.

## Structure

The following functions are used:

### _isComplete_

Checks if the puzzle is complete and returns this as a Boolean. This is used to determine when the puzzle has been successfully solved and the main algoirhtm continues to iterate until this condition is met.

### _isValid_

Looks at the contents of each row, column anf box in the puzzle and uses the _duplicatesExist_ function to check if the current puzzle state is valid, returning a Boolean.

### _duplicatesExist_

Takes a list as input and checks for duplicate values, returning this as a Boolean.

### _showGrid_

Prints out a given puzzle grid to the console. This functionns prints out the incomplete grid at the beginning and then the completed version at the end. However, it was also useful for the testing process.

## Algorithm

The algorithm uses an iterative backtracking approach that cycles through potential solutions until the puzzle reaches a state where it is valid and fully completed. Starting with the first unfilled square, the value is incremented and the _isValid_ function checks that this state is allowed. If the state is illegal then the value is incremented again until it becomes valid. If the state is legal, the algorithm moves on to the next unfilled square and repeats the process. If there comes a point where every potential value for an unfilled square is illegal then backtracking occurs and the algorithm reverts earlier decisions until progress can be made.

## Evaluation

