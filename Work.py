#  File: Work.py

#  Description: Figures out how many lines to code through binary search and linear search

#  Student Name:  Riley Sample

#  Student UT EID:  rcs3396

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 2/21/22

#  Date Last Modified: 2/21/22

import sys, time

"""This is how he plans to write the program. He will write the first v lines of code, 
then drink his first cup of coffee. Since his productivity has gone down by a factor of 
k he will write v // k lines of code. He will have another cup of coffee and then write v // k**2 lines of code. 
He will have another cup of coffee and write v // k**3 lines of code and so on. He will collapse and fall asleep 
when v // k ** p becomes 0."""


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
    # use linear search here
    for i in range(1, n + 1):
        if num_lines(i, k) >= n:
            return i

    return -1


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be
#         written before the first cup of coffee
def binary_search(n: int, k: int) -> int:
    # use binary search here
    upper = n
    lower = 1
    while lower <= upper:
        middle = (upper + lower) // 2
        lines = num_lines(middle, k)

        if lines < n:
            lower = middle + 1
        elif lines > n:
            upper = middle - 1
        else:
            return middle

    return -1


# calculates the number of lines after each cup of coffee
def num_lines(v, k):
    cntr = 1
    lines = v
    while (v // k**cntr) != 0:
        lines += v // k**cntr
        cntr += 1

    return lines


# main has been completed for you
# do NOT change anything below this line
def main():
    num_cases = int((sys.stdin.readline()).strip())

    for i in range(num_cases):
        inp = (sys.stdin.readline()).split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()


# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
