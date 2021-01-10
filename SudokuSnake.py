
import numpy
from math import floor


def PrintPuzzle (grid):

  line = " "
  for squareX in range(3):
    line += "---------"
    if squareX < 2:
      line += "-"
    else:
      line += " "
  print (line)

  for squareY in range(3):
    for row in range(3):
      line = "|"
      for squareX in range(3):
        for col in range(3):
          line += "   "
        line += "|"
      print (line)

      line = "|"
      for squareX in range(3):
        for col in range(3):
          line += " " + str(grid[row+3*squareY][col+3*squareX]) + " "
        line += "|"
      print (line)

      if row == 2:
        line = "|"
        for squareX in range(3):
          for col in range(3):
            line += "   "
          line += "|"
        print (line)

    if squareY < 2:
      line = "-"
      for squareX in range(3):
        line += "----------"
      print (line)
    else:
      line = " "
      for squareX in range(3):
        line += "---------"
        if squareX < 2:
          line += "-"
        else:
          line += " "
      print (line)
    


def CheckPosition (row, col, grid):
  vals=[]

  for i in range(1,10):
    goodVal = True

    # first check same row
    for j in range(9):
      if grid[row][j] == i:
        goodVal = False

    # then check same column
    for j in range(9):
      if grid[j][col] == i:
        goodVal = False

    # finally check same box
    rowMod = floor (row / 3) * 3
    colMod = floor (col / 3) * 3
    for j in range (rowMod, rowMod+2):
      for k in range (colMod, colMod+2):
        if grid[j][k] == i:
          goodVal = False

    # if still a good value, add it to the list
    if goodVal:
      vals.append (i)

  return vals



def SolveNewCell (grid):
  for i in range (9):
    for j in range (9):
      if grid[i][j] != -1:
        continue;
      vals = CheckPosition (i, j, grid)

      if len(vals) == 1:
        return (i,j,vals[0])

  return (-1,-1,-1)
  


def SudokuSnake (filename):

  debug = 1
 
  grid = numpy.genfromtxt(filename,dtype=int)

  numUnks = 0
  for i in range (9):
    for j in range (9):
      assert (grid[i][j] >= 1 and grid[i][j] <= 9) or (grid[i][j] == -1)
      if grid[i][j] == -1:
        numUnks += 1

  print("Num. unknowns: " + str(numUnks))


  while (numUnks > 0):
    
    result = SolveNewCell (grid)

    if result[2] == -1:
      if debug > 1:
        print ("Unable to solve? Please check grid:")
      if debug > 2:
        print (grid)

    if debug > 1:
      print("Solved row " + str(result[0]) + ", column " + str(result[1]) + ", value = " + str(result[2])) 
    grid[result[0]][result[1]] = result[2]

    numUnks -= 1


  print ("Final solved puzzle:")
  PrintPuzzle(grid)


