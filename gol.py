from random import randint

# Init 2-d array
ROWS = 10
COLS = 10

# compute next step
def computeNext(grid):
    nextGrid = getEmptyGrid()
    for i in xrange(ROWS):
        for j in xrange(COLS):
            numNeighbours = getNumNeighbours(grid, i, j)
            if (numNeighbours > 4):
                nextGrid[i][j] = 0
            elif numNeighbours < 2:
                nextGrid[i][j] = 0
            elif numNeighbours == 3:
                nextGrid[i][j] = 1
    return nextGrid


def printGrid(grid):
    print "-----"
    for i in xrange(ROWS):
        print grid[i]


def getEmptyGrid():
    return [[0 for x in xrange(COLS)] for y in xrange(ROWS)]
    

def getRandomGrid():
    grid = [[None for x in range(COLS)] for y in range(ROWS)]
    for i in xrange(ROWS):
        for j in xrange(COLS):
            grid[i][j] = randint(0, 1)
    return grid


def getNumNeighbours(grid, i, j):
    # top left
    if i == 0 and j == 0:
        numNeighbours = grid[i][j+1] + grid[i+1][j] + grid[i+1][j+1]
    elif i == 0 and j == COLS-1:
       numNeighbours = grid[0][COLS-2] + grid[1][COLS-2] + grid[1][COLS-1]
    else:
       numNeighbours = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + \
                                 grid[i][j-1] + grid[i][j+1] + \
                                 grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
                                  

# main
g = getRandomGrid()
i = 0
while(i < 3):
    printGrid(g)
    ng = computeNext(g)
    g = ng
    i = i + 1
