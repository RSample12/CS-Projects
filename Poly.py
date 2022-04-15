#  File: Poly.py

#  Description: Linked List representation of polynomials

#  Student Name: Riley Sample

#  Student UT EID: rcs3396

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 4/7/22

#  Date Last Modified: 4/7/22

import sys


class Link(object):
    def __init__(self, coeff=1, exp=1, next=None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__(self):
        return '(' + str(self.coeff) + ', ' + str(self.exp) + ')'


class LinkedList(object):
    def __init__(self):
        self.first = None

    # get number of links without coeff of 0
    def get_num_links(self):
        cur = self.first
        if cur is None:
            return 0

        cntr = 0
        while cur:
            if cur.coeff != 0:
                cntr += 1
            cur = cur.next
        return cntr

    # insert link at the front
    def insert_first(self, coeff, exp):
        first = Link(coeff, exp)
        first.next = self.first
        self.first = first

    # insert link at the end
    def insert_last(self, coeff, exp):
        last = Link(coeff, exp)
        cur = self.first
        if cur is None:
            self.first = last
            return
        while cur.next:
            cur = cur.next
        cur.next = last

    # keep Links in descending order of exponents, adds if same exponent
    def insert_in_order(self, coeff, exp):
        link = Link(coeff, exp)
        prev = self.first
        cur = self.first

        # compares to first link/ checks for empty list
        if cur is None or cur.exp < exp:
            self.insert_first(coeff, exp)
            return
        elif cur.exp == exp:
            cur.coeff += coeff
            return

        # compares to rest of list and places in proper spot or adds if exponents are equal
        while cur:
            if cur.exp < exp:
                break
            elif cur.exp == exp:
                cur.coeff += coeff
                return
            prev = cur
            cur = cur.next
        prev.next = link
        link.next = cur

    # copies list and returns new list
    def copy_list(self):
        new_list = LinkedList()
        cur = self.first
        if cur is None:
            return new_list

        while cur:
            new_list.insert_last(cur.coeff, cur.exp)
            cur = cur.next

        return new_list

    # add polynomial p to this polynomial and return the sum
    def add(self, p):
        new_list = p.copy_list()

        cur = self.first
        while cur:
            new_list.insert_in_order(cur.coeff, cur.exp)
            cur = cur.next

        return new_list

    # multiply polynomial p to this polynomial and return the product
    def mult(self, p):
        new_list = LinkedList()

        cur = self.first
        while cur:
            p_cur = p.first
            while p_cur:
                coeff = cur.coeff * p_cur.coeff
                exp = cur.exp + p_cur.exp
                new_list.insert_in_order(coeff, exp)
                p_cur = p_cur.next
            cur = cur.next

        return new_list

    # create a string representation of the polynomial
    def __str__(self):
        string = ""
        cur = self.first

        # if only one link returns the first link without coeff of 0
        if self.get_num_links() == 1:
            while cur:
                if cur.coeff != 0:
                    return "(" + str(cur.coeff) + ", " + str(cur.exp) + ")"
                cur = cur.next

        cur = self.first
        while cur.next:
            if cur.coeff != 0:
                string += "(" + str(cur.coeff) + ", " + str(cur.exp) + ") + "
            cur = cur.next

        if cur.coeff != 0:
            string += "(" + str(cur.coeff) + ", " + str(cur.exp) + ")"

        return string


def main():
    # read data from file poly.in from stdin
    num = int(sys.stdin.readline())
    poly = []
    for i in range(num):
        line = sys.stdin.readline()
        temp = line.strip().split()
        poly.append(temp)

    sys.stdin.readline()

    num = int(sys.stdin.readline())
    poly2 = []
    for i in range(num):
        line = sys.stdin.readline().strip("\n")
        temp = line.split()
        poly2.append(temp)

    # create polynomial p
    p = LinkedList()
    for var in poly2:
        p.insert_in_order(int(var[0]), int(var[1]))

    # create polynomial q
    q = LinkedList()
    for var in poly:
        q.insert_in_order(int(var[0]), int(var[1]))

    # get sum of p and q and print sum
    poly_sum = p.add(q)
    print(poly_sum)

    # get product of p and q and print product
    poly_mult = p.mult(q)
    print(poly_mult)


if __name__ == "__main__":
    main()
