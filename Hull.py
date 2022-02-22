#  File: Hull.py

#  Description:

#  Student's Name: Riley Sample

#  Student's UT EID: rcs3396

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 2/17/22

#  Date Last Modified:

import sys
import math


class Point(object):
    # constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
    def __eq__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __ne__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y < other.y)
        return (self.x < other.x)

    def __le__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y <= other.y)
        return (self.x <= other.x)

    def __gt__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y > other.y)
        return (self.x > other.x)

    def __ge__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y >= other.y)
        return (self.x >= other.x)


def sort_points(points):
    # sort list by x value
    for i in range(1, len(points)):
        while points[i - 1].x > points[i].x and i > 0:
            points[i - 1], points[i] = points[i], points[i - 1]
            # if tuples_list[i-1]:
            i -= 1

    return points


def det(p, q, r):
    # determinant
    det = (p.x * q.y) + (q.x * r.y) + (r.x * p.y) - (p.y * q.x) - (q.y * r.x) - (r.y * p.x)

    if det == 0:
        return "straight"
    elif det < 0:
        return "right"
    elif det > 0:
        return "left"


def area_poly(hull):
    # det = (x1 * y2 + x2 * y3 + ... + xn * y1 - y1 * x2 - y2 * x3 - ... - yn * x1)
    det = 0

    # first half of equation
    for i in range(0, len(hull)):
        if i == len(hull) - 1:
            det += (hull[i].x * hull[0].y)
        else:
            det += (hull[i].x * hull[i + 1].y)

    # second half
    for i in range(0, len(hull)):
        if i == len(hull) - 1:
            det -= (hull[i].y * hull[0].x)
        else:
            det -= (hull[i].y * hull[i + 1].x)

    area = (1 / 2) * abs(det)
    return area


def convex_hull(point_list):

    # create upper hull
    upper_hull = [point_list[0], point_list[1]]
    for i in range(2, len(point_list)):
        upper_hull.append(point_list[i])
        while len(upper_hull) >= 3 and det(upper_hull[-3], upper_hull[-1], upper_hull[-2]) != "right":
            upper_hull.pop(-2)

    # lower hull
    lower_hull = [point_list[-1], point_list[-2]]
    for i in range(len(point_list) - 2, -1, -1):
        lower_hull.append(point_list[i])
        while len(lower_hull) >= 3 and det(lower_hull[-3], lower_hull[-1], lower_hull[-2]) != "right":
            lower_hull.pop(-2)

    # combine upper and lower hull
    lower_hull.pop(0)
    lower_hull.pop(-1)
    upper_hull.extend(lower_hull)
    hull = [upper_hull.pop(0)]
    hull.extend(reversed(upper_hull))

    return hull


def main():
    # Input: A set of point objects in the x-y plane.
    num_lines = sys.stdin.readline()
    file = sys.stdin.readlines()
    point_list = []
    # read file and create new point for each line
    for line in file:
        temp_str = line.strip("\n")
        temp = temp_str.split()
        point_list.append(Point(int(temp[0]), int(temp[1])))

    #Output
    point_list = sort_points(point_list)
    hull = convex_hull(point_list)
    area = area_poly(hull)

    sys.stdout.write("Convex Hull\n")
    for point in hull:
        sys.stdout.write(f"({point.x}, {point.y})\n")

    sys.stdout.write(f"\nArea of Convex Hull = {area}")


if __name__ == "__main__":
    main()
