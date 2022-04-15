#  File: Triangle.py

#  Description: Uses different measures speed and accuracy of different algorithms in finding max sum of triangle

#  Student Name: Riley Sample

#  Student UT EID: rcs3396

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 3/4/22

#  Date Last Modified: 3/28/22

import sys

from timeit import timeit


# Brute force helper function
def bf_helper(grid, row, col, sum, lst):
    sum += grid[row][col]

    # If a path reaches end of the tree, add to list
    if row == len(grid) - 1:
        lst.append(sum)
    else:
        # Check next two branches
        bf_helper(grid, row + 1, col, sum, lst)
        bf_helper(grid, row + 1, col + 1, sum, lst)


# returns the greatest path sum using exhaustive search
def brute_force(grid):
    lst = []
    bf_helper(grid, 0, 0, 0, lst)
    return max(lst)


# returns the greatest path sum using greedy approach
def greedy(grid):
    sum = grid[0][0]
    col = 0

    # Follows path of max branch
    for row in range(len(grid) - 1):
        branch1 = grid[row + 1][col]
        branch2 = grid[row + 1][col + 1]
        if branch1 > branch2:
            sum += branch1
        else:
            sum += branch2
            col += 1

    return sum


# Divide and conquer helper function
def dc_helper(grid, row, col, sum):

    if row == len(grid) - 1:
        return sum

    else:
        branch1 = grid[row + 1][col]
        branch2 = grid[row + 1][col + 1]
        return max(dc_helper(grid, row + 1, col, sum + branch1), dc_helper(grid, row + 1, col + 1, sum + branch2))


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer(grid):
    sum = grid[0][0]
    return dc_helper(grid, 0, 0, sum)


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):

    for row in reversed(range(len(grid))):
        prev_root = 0
        for col in reversed(range(len(grid[0]))):

            # Checks root of branch the loop is looking at, if it is the same, ignore
            root = grid[row - 1][col - 1]
            if grid[row][col] != 0 and root != prev_root:
                prev_root = root

                # Checks which branch is greater and adds to the respective root in grid
                if grid[row][col] > grid[row][col - 1]:
                    grid[row - 1][col - 1] += grid[row][col]
                else:
                    grid[row - 1][col - 1] += grid[row][col - 1]

    return grid[0][0]


# reads the file and returns a 2-D list that represents the triangle
def read_file():
    # read number of lines
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create an empty grid with 0's
    grid = [[0 for i in range(n)] for j in range(n)]

    # read each line in the input file and add to the grid
    for i in range(n):
        line = sys.stdin.readline()
        line = line.strip()
        row = line.split()
        row = list(map(int, row))
        for j in range(len(row)):
            grid[i][j] = grid[i][j] + row[j]

    return grid


def main():
    # read triangular grid from file
    grid = read_file()

    # check that the grid was read in properly
    # print (grid)

    # output greatest path from exhaustive search
    times = timeit('brute_force({})'.format(grid), 'from __main__ import brute_force', number=10)
    times = times / 10
    # print time taken using exhaustive search
    print("The greatest path sum through exhaustive search is")
    print(brute_force(grid))
    print("The time taken for exhaustive search in seconds is")
    print(times)

    # output greatest path from greedy approach
    times = timeit('greedy({})'.format(grid), 'from __main__ import greedy', number=10)
    times = times / 10
    # print time taken using greedy approach
    print("The greatest path sum through greedy search is")
    print(greedy(grid))
    print("The time taken for greedy approach in seconds is")
    print(times)

    # output greatest path from divide-and-conquer approach
    times = timeit('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number=10)
    times = times / 10
    # print time taken using divide-and-conquer approach
    print("The greatest path sum through recursive search is")
    print(divide_conquer(grid))
    print("The time taken for recursive search in seconds is")
    print(times)

    # output greatest path from dynamic programming
    times = timeit('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number=10)
    times = times / 10
    # print time taken using dynamic programming
    print("The greatest path sum through dynamic programming is")
    print(dynamic_prog(grid))
    print("The time taken for dynamic programming in seconds is")
    print(times)


if __name__ == "__main__":
    main()
