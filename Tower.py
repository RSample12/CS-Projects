#  File: Tower.py

#  Description:

#  Student's Name: Riley Sample

#  Student's UT EID: rcs3396

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 3/7/22

#  Date Last Modified:

import sys
import math


# Input: n the number of disks
# Output: returns the number of transfers using four needles
def num_moves(n):
    k = round(n - (math.sqrt(2 * n + 1)) + 1)
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (2**(n - k) - 1) + (2 * num_moves(k))


def main():
    # read number of disks and print number of moves
    for line in sys.stdin:
        line = line.strip()
        num_disks = int(line)
        print(num_moves(num_disks))


if __name__ == "__main__":
    main()
