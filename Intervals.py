#  File: Intervals.py

#  Description:

#  Student Name: Riley Sample

#  Student UT EID: rcs3396

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 1/30/22

#  Date Last Modified:

import sys


# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples(tuples_list):
    print(tuples_list)
    new_list = []

    # sort list
    for i in range(1, len(tuples_list)):
        while tuples_list[i-1][0] > tuples_list[i][0] and i > 0:
            tuples_list[i-1], tuples_list[i] = tuples_list[i], tuples_list[i-1]
            # if tuples_list[i-1]:
            i -= 1
    print(tuples_list)

    # merge list
    for i in range(1, len(tuples_list)):
        if tuples_list[i][0] < tuples_list[i+1][0] and :


    # Input: tuples_list is a list of tuples of denoting intervals
    # Output: a list of tuples sorted by ascending order of the size of
    #         the interval
    #         if two intervals have the size then it will sort by the
    #         lower number in the interval


# def sort_by_interval_size (tuples_list):

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
    assert merge_tuples([(1, 2)]) == [(1, 2)]
    # write your own test cases

    assert sort_by_interval_size([(1, 3), (4, 5)]) == [(4, 5), (1, 3)]
    # write your own test cases
    assert sort_by_interval_size([(1, 3), (1, 2), (1, 5), (1, 4)]) == [(1, 2), (1, 3), (1, 4), (1, 5)]

    return "all test cases passed"


def main():
    # open file intervals.in and read the data and create a list of tuples
    tup_lst = []
    num_lines = int(sys.stdin.readline())
    file = sys.stdin.readlines()

    for line in file:
        tup = (int(line.split()[0]), int(line.split()[1]))
        tup_lst.append(tup)

    # print(tup_lst)

    # merge the list of tuples
    print(merge_tuples(tup_lst))
    # sort the list of tuples according to the size of the interval
    # print(sort_by_interval_size(tup_lst))
    # run your test cases
    '''
    print (test_cases())
    '''

    # write the output list of tuples from the two functions


if __name__ == "__main__":
    main()
