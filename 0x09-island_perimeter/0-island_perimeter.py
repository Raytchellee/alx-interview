#!/usr/bin/python3
""" Island perimeter """


def island_perimeter(grid):
    """Island perimeter function"""
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for idx in range(rows):
        for idy in range(cols):
            if grid[idx][idy] == 1:
                perimeter += 4
                if idx > 0 and grid[idx - 1][idy] == 1:
                    perimeter -= 2
                if idy > 0 and grid[idx][idy - 1] == 1:
                    perimeter -= 2

    return perimeter
