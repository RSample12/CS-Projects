#  File: TestBinaryTree.py

#  Description: Create binary tree functions

#  Student Name: Riley Sample

#  Student UT EID: rcs3396

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 4/14/22

#  Date Last Modified: 4/15/22

import sys


class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

    def __str__(self):
        return str(self.data)


class Tree(object):
    def __init__(self):
        self.root = None

        # Insert a node in the tree

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            curr = self.root
            parent = curr
            while curr:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild

            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node

    # Returns true if two binary trees are similar
    def is_similar(self, pNode):

        def sim_helper(node1, node2):
            if node1 is None or node2 is None:
                if node1 is None and node2 is None:
                    return True
                else:
                    return False

            else:
                if node1.data == node2.data:
                    return sim_helper(node1.lChild, node2.lChild) and sim_helper(node1.rChild, node2.rChild)
                else:
                    return False

        return sim_helper(self.root, pNode.root)

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        if self.root is None:
            return []
        else:
            tree = self.get_tree()
            nodes = tree[level]
            return nodes

    # Returns the height of the tree
    def get_height(self):

        def height_helper(aNode, height):
            if aNode is None:
                return height - 1

            return max(height_helper(aNode.lChild, height + 1), height_helper(aNode.rChild, height + 1))

        return height_helper(self.root, 0)

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes(self):

        def nodes_helper(aNode):
            if aNode is None:
                return 0

            return 1 + nodes_helper(aNode.lChild) + nodes_helper(aNode.rChild)

        return nodes_helper(self.root)

    # returns tree as list of lists by level
    def get_tree(self):
        nodes = []
        Q = []

        Q.append(self.root)
        Q.append("level")
        temp = []
        while len(Q) > 1:

            curr = Q.pop(0)
            if curr == "level":
                nodes.append(temp)
                temp = []
                Q.append("level")

            else:
                if curr.lChild:
                    Q.append(curr.lChild)
                if curr.rChild:
                    Q.append(curr.rChild)
                temp.append(curr)

        nodes.append(temp)
        return nodes


def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line))  # converts elements into ints

    tree1 = Tree()
    for i in tree1_input:
        tree1.insert(i)

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line))  # converts elements into ints

    tree2 = Tree()
    for i in tree2_input:
        tree2.insert(i)

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line))  # converts elements into ints

    tree3 = Tree()
    for i in tree3_input:
        tree3.insert(i)

    # Test your method is_similar()
    print(tree1.is_similar(tree2))
    print(tree1.is_similar(tree3))

    # Print the various levels of two of the trees that are different

    # Get the height of the two trees that are different
    print(tree1.get_height())
    print(tree3.get_height())

    # Get the total number of nodes a binary search tree
    print(tree1.num_nodes())
    print(tree3.num_nodes())


if __name__ == "__main__":
    main()
