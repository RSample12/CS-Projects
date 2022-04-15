#  File: TestLinkedList.py

#  Description: functions for linked list

#  Student Name: Riley Sample

#  Student UT EID: rcs3396

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 4/4/22

#  Date Last Modified: 4/5/22

class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList(object):
    # create a linked list
    # you may add other attributes
    def __init__(self):
        self.first = None

    # get number of links
    def get_num_links(self):
        cur = self.first
        if cur is None:
            return 0

        cntr = 0
        while cur:
            cntr += 1
            cur = cur.next
        return cntr

    # add an item at the beginning of the list
    def insert_first(self, data):
        first = Link(data)
        first.next = self.first
        self.first = first

    # add an item at the end of a list
    def insert_last(self, data):
        last = Link(data)
        cur = self.first
        if cur is None:
            self.first = last
            return
        while cur.next:
            cur = cur.next
        cur.next = last

    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order(self, data):
        link = Link(data)
        prev = self.first
        cur = self.first
        if cur is None or data <= self.first.data:
            self.insert_first(data)
            return

        while cur:
            if cur.data >= data:
                break
            prev = cur
            cur = cur.next

        prev.next = link
        link.next = cur

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        cur = self.first
        if cur is None:
            return None
        elif cur.data == data:
            return cur

        while cur:
            if cur.data == data:
                return cur
            cur = cur.next

        return None

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        cur = self.first
        if cur is None:
            return None
        elif cur.data == data:
            return cur

        while cur:
            if cur.data == data:
                return cur
            cur = cur.next

        return None

    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link(self, data):
        prev = self.first
        cur = self.first
        if self.find_unordered(data) is None:
            return None
        elif cur.data == data:
            self.first = self.first.next

        while cur:
            if cur.data == data:
                prev.next = cur.next
                return cur
            prev = cur
            cur = cur.next

        return None

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        cntr = 0
        string = ""
        cur = self.first
        if self.is_empty():
            return ""

        while cur:
            if cntr % 10 == 0 and cntr != 0:
                string += "\n"
            string += str(cur.data) + "  "
            cntr += 1
            cur = cur.next

        return string

    # Copy the contents of a list and return new list
    # do not change the original list
    def copy_list(self):
        new_list = LinkedList()
        if self.is_empty():
            return new_list

        cur = self.first
        while cur:
            new_list.insert_last(cur.data)
            cur = cur.next

        return new_list

    # Reverse the contents of a list and return new list
    # do not change the original list
    def reverse_list(self):
        new_list = LinkedList()

        cur = self.first
        while cur:
            new_list.insert_first(cur.data)
            cur = cur.next

        return new_list

    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list(self):
        new_list = LinkedList()
        if self.is_empty():
            return new_list

        cur = self.first
        for i in range(self.get_num_links()):
            if i == 0:
                new_list.insert_first(cur.data)
            else:
                new_list.insert_in_order(cur.data)
            cur = cur.next

        return new_list

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        if self.is_empty():
            return True

        prev = self.first
        cur = self.first
        while cur.next:
            cur = cur.next
            if cur.data < prev.data:
                return False
            prev = prev.next

        return True

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        if self.get_num_links() == 0:
            return True
        return False

    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list(self, other):
        new_list = other.copy_list()

        cur = self.first
        while cur:
            new_list.insert_in_order(cur.data)
            cur = cur.next

        return new_list

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        if self.get_num_links() != other.get_num_links():
            return False

        self_cur = self.first
        other_cur = other.first
        while self_cur:
            if self_cur.data != other_cur.data:
                return False
            self_cur = self_cur.next
            other_cur = other_cur.next

        return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list
    def remove_duplicates(self):
        new_list = LinkedList()
        if self.is_empty():
            return new_list

        cur = self.first
        while cur:
            if new_list.find_unordered(cur.data) is None:
                new_list.insert_last(cur.data)
            cur = cur.next

        return new_list


def main():
    pass
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    print("Test insert_first and str")
    new_list = LinkedList()
    for i in range(15):
        new_list.insert_first(i)
    print(new_list)
    print()

    # Test method insert_last()
    print("Test insert_last")
    new_list = LinkedList()
    for i in range(15):
        new_list.insert_last(i)
    print(new_list)
    print()

    # Test method insert_in_order()
    print("Test insert_in_order")
    new_list.insert_in_order(3)
    new_list.insert_in_order(5)
    new_list.insert_in_order(18)
    print(new_list)
    print()

    # Test method get_num_links()
    print("Test get_num_linked")
    print(new_list.get_num_links())
    print()

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    print("Test find_unordered()")
    print(new_list.find_unordered(7))
    print(new_list.find_unordered(18))
    print()

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    print("Test find_ordered()")
    print(new_list.find_ordered(7))
    print(new_list.find_ordered(18))
    print()

    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    print("Test delete_link")
    print(new_list)
    print(new_list.delete_link(5))
    print(new_list)
    print(new_list.delete_link(0))
    print(new_list)
    print()

    # Test method copy_list()
    print("Test copy_list")
    copied = new_list.copy_list()
    print(copied)
    print()

    # Test method reverse_list()
    print("Test reverse_list")
    reverse = copied.reverse_list()
    print(reverse)
    print()

    # Test method sort_list()
    print("Test sort_list")
    unsorted = LinkedList()
    unsorted.insert_last(8)
    unsorted.insert_last(3)
    unsorted.insert_last(9)
    unsorted.insert_last(4)
    unsorted.insert_last(1)
    unsorted.insert_last(6)
    print(unsorted)
    sorted = unsorted.sort_list()
    print(sorted)
    print()

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print("Test is_sorted")
    print(unsorted.is_sorted())
    print(sorted.is_sorted())
    print()

    # Test method is_empty()
    print("Test is_empty")
    empty = LinkedList()
    print(empty.is_empty())
    empty.insert_last(1)
    empty.insert_last(4)
    print(empty.is_empty())
    print()

    # Test method merge_list()
    print("Test merge_list")
    list1 = LinkedList()
    list2 = LinkedList()
    list1.insert_last(1)
    list2.insert_last(2)
    list1.insert_last(3)
    list2.insert_last(4)
    merged = list1.merge_list(list2)
    print(list1)
    print(list2)
    print(merged)
    print()

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print("Test is_equal")
    list1 = LinkedList()
    list2 = LinkedList()
    for i in range(5):
        list1.insert_last(i)
        list2.insert_last(i)
    print(list1.is_equal(list2))
    list1 = LinkedList()
    list1.insert_last(5)
    list1.insert_last(3)
    print(list1.is_equal(list2))
    print()

    # Test remove_duplicates()
    print("Test remove_duplicates")
    print(new_list)
    print(new_list.remove_duplicates())


if __name__ == "__main__":
    main()
