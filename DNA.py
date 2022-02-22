
#  File: DNA.py

#  Description: Finds largest subsequence between 2 strings

#  Student Name: Riley Sample

#  Student UT EID: rcs3396

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 1/20/22

#  Date Last Modified: 1/22/22

import sys


# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.
def longest_subsequence(s1, s2):
    cntr = len(s1)
    temp = []

    # fill temp array with all possible substrings of s1 that are also in s2
    while cntr > 0:
        index = 0
        while index + cntr <= len(s1):
            if s1[index:index + cntr] in s2:
                temp.append(s1[index:index + cntr])
            index += 1
        cntr -= 1

    # create new array and add the longest non-duplicate substrings
    longest = []
    for i in temp:
        if len(i) == len(temp[0]) and i not in longest:
            longest.append(i)

    # sort longest by alphabetical order and return
    longest.sort()
    return longest

def main():
    # read the number of pairs
    num_pairs = sys.stdin.readline()
    num_pairs = num_pairs.strip()
    num_pairs = int(num_pairs)

    # for each pair call the longest_subsequence
    for i in range(num_pairs):
        st1 = sys.stdin.readline()
        st2 = sys.stdin.readline()

        st1 = st1.strip()
        st2 = st2.strip()

        st1 = st1.upper()
        st2 = st2.upper()

        # get the longest subsequences
        long_sub = longest_subsequence(st1, st2)

        # print the result
        for x in long_sub:
            print(x)
        # insert blank line
        print()


if __name__ == "__main__":
    main()
