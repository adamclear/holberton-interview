#!/usr/bin/python3
''' 0-island_perimeter task '''


def island_perimeter(grid):
    '''  Calculate the perimeter of an island on a rectangular grid
     of 0s and 1s. '''
    perimeter = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 1:
                if x == 0:
                    perimeter += 1
                else:
                    if grid[x - 1][y] == 0:
                        perimeter += 1
                if x == len(grid) - 1:
                    perimeter += 1
                else:
                    if grid[x + 1][y] == 0:
                        perimeter += 1
                if y == 0:
                    perimeter += 1
                else:
                    if grid[x][y - 1] == 0:
                        perimeter += 1
                if y == len(grid[x]) - 1:
                    perimeter += 1
                else:
                    if grid[x][y + 1] == 0:
                        perimeter += 1
    return perimeter
