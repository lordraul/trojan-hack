# ..
# >^

# [ [ None, None ], [ Right, Up ] ] -> allsoldiers = [ (1, 0), (1,1) ]
# soldiers - len(allSoldiers)

from enum import Enum
from soldier import Soldier, Direction
import random as rand

class ExitType(Enum):
    TL = 0
    BR = 1
    A = 2 

def Generate(tiles: tuple[int, int] = (10, 10)):
    exitrows = []
    exitcols = []

    for i in range(tiles[0]):
        if rand.randint(1, 3) != 1:
            exitrows.append((i, ExitType(rand.randint(0,2))))
     
    for i in range(tiles[1]):
        if rand.randint(1, 3) != 1:
            exitcols.append((i, ExitType(rand.randint(0,2))))
    
    grid = [[None for _ in range(tiles[0])] for _ in range(tiles[1])]
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            for pos in exitrows:
                if(r == pos[0]):
                    match pos[1].value:
                        case 0:
                            grid[r][c] = Direction.LEFT
                        case 1:
                            grid[r][c] = Direction.LEFT
                        case 2:
                            if(c < (len(grid[r]) / 2)):
                                grid[r][c] = Direction.LEFT
                            else:
                                grid[r][c] = Direction.RIGHT
            for pos in exitcols:
                if(c == pos[0]):
                    match pos[1].value:
                        case 0:
                            if(grid[r][c] != None):
                                if(rand.randint(0, 1)):
                                    grid[r][c] = Direction.UP
                            else:
                                grid[r][c] = Direction.UP
                        case 1:
                            if(grid[r][c] != None):
                                if(rand.randint(0, 1)):
                                    grid[r][c] = Direction.DOWN
                            else:
                                grid[r][c] = Direction.DOWN
                        case 2:
                            if(grid[r][c] != None):
                                if(rand.randint(0, 1)):
                                    if(r < (len(grid[c]) / 2)):
                                        grid[r][c] = Direction.UP
                                    else:
                                        grid[r][c] = Direction.DOWN
                            else:
                                if(r < (len(grid[c]) / 2)):
                                    grid[r][c] = Direction.UP
                                else:
                                    grid[r][c] = Direction.DOWN

    return (grid, exitcols, exitrows)