#  File: ExpressionTree.py

#  Description: Creates tree modeling expression

#  Student Name: Riley Sample

#  Student UT EID: rcs3396

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 4/11/22

#  Date Last Modified: 4/11/22

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # check if the queue if empty
    def is_empty(self):
        return len(self.queue) == 0


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

    def __str__(self):
        return str(self.data)


class Tree(object):
    def __init__(self):
        self.root = Node()

    # this function takes in the input string expr and
    # creates the expression tree
    def create_tree(self, expr):
        current_node = self.root
        node_stack = Stack()
        # split for float values
        expr = expr.split()

        for token in expr:
            if token == "(":
                current_node.lChild = Node()
                node_stack.push(current_node)
                current_node = current_node.lChild
            elif token in operators:
                current_node.data = token
                node_stack.push(current_node)
                current_node.rChild = Node()
                current_node = current_node.rChild
            elif token == ")":
                if not node_stack.is_empty():
                    current_node = node_stack.pop()
            else:
                current_node.data = token
                current_node = node_stack.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    # ['+', '-', '*', '/', '//', '%', '**']
    def evaluate(self, aNode):
        data = aNode.data

        if data in operators:
            if data == "+":
                return self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild)
            elif data == "-":
                return self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild)
            elif data == "*":
                return self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild)
            elif data == "/":
                return self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild)
            elif data == "//":
                return self.evaluate(aNode.lChild) // self.evaluate(aNode.rChild)
            elif data == "%":
                return self.evaluate(aNode.lChild) % self.evaluate(aNode.rChild)
            elif data == "**":
                return self.evaluate(aNode.lChild) ** self.evaluate(aNode.rChild)

        else:
            return float(eval(data))

    # this function should generate the preorder notation of
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order(self, aNode):
        if aNode:
            return [aNode.data] + self.pre_order(aNode.lChild) + self.pre_order(aNode.rChild)
        return []

    # this function should generate the postorder notation of
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order(self, aNode):
        if aNode:
            return self.post_order(aNode.lChild) + self.post_order(aNode.rChild) + [aNode.data]
        return []

    # prints tree
    def print_tree(self):
        nodes = []
        Q = []

        Q.append(self.root)
        Q.append("level")
        temp = []
        while len(Q) > 1:

            curr = Q.pop(0)
            print(curr)
            if curr == "level":
                nodes.append(temp)
                temp = []
                Q.append("level")

            else:
                if curr.lChild:
                    Q.append(curr.lChild)
                if curr.rChild:
                    Q.append(curr.rChild)
                temp.append(str(curr))

        nodes.append(temp)

        return nodes


# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)
    nodes = tree.print_tree()
    for i in nodes:
        print(i)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", " ".join(tree.pre_order(tree.root)))

    # get the postfix version of the expression and print
    print("Postfix Expression:", " ".join(tree.post_order(tree.root)))


if __name__ == "__main__":
    main()
