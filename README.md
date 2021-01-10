# SudokuSnake

Jeff Ouellette
Jan. 10th 2020

I got bored on a Sunday so I wrote a Sudoku solver in python. It's probably not very efficient but should be able to figure out any Sudoku you give it in the form of a dat file (see "test.dat" for an example).

All "unknown" values are initialized to -1, for lack of something better. Theres probably a better way to do this -- i.e. use a csv or something which can store null entries, but whatever.

To use the solver, run in Python (requires numpy -- again, you could probably write this to just run on python lists, but :man_shrugging:) with the following commands:

> python
> import SudokuSnake
> SudokuSnake.SudokuSnake ("test.dat")
