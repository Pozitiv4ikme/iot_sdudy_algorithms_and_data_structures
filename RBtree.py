from Node import *


# Properties of red-black tree
# 1. All nodes have color: red or black
# 2. Root of tree and all leafs are black
# 3. If node is red - two her child black (otherwise, parent of red node is black)
# 4. Each path from the root to a leaf node must pass through the same number of black vertices
class RBtree:

    # create leaf - NIL node and set root like leaf
    # because when we create tree it should be empty
    def __init__(self):
        self.LEAF = Node(0)
        self.LEAF.right = None
        self.LEAF.left = None
        self.LEAF.color = NodeColor.BLACK
        self.root = self.LEAF

    def left_rotate(self, node):
        # x = node
        y = node.right

        # first step
        node.right = y.left
        if y.left is not self.LEAF:
            y.left.parent = node

        # second step
        if node.parent is None:
            self.root = y

        # find the side of x by his parent and put here y
        # it is like node swap and make y like root
        elif node.parent.left == node:
            node.parent.left = y
        else:
            node.parent.right = y

        # third step
        y.left = node

        # fourth step
        node.parent = y

    def right_rotate(self, node):
        y = node.right

        y.left = node.right
        if node.right is not self.LEAF:
            node.left.parent = y
        elif y.parent.left == y:
            y.parent.left = node
        else:
            y.parent.right = node

        node.right = y
        y.parent = node

    # insert node
    def insert(self, insertion_node_value):

        # initialize the node to insert
        insertion_node = Node(insertion_node_value)
        insertion_node.right = self.LEAF
        insertion_node.left = self.LEAF
        insertion_node.parent = None

        # create temp variable for rotate
        y = None
        x = self.root

        # traversing the tree to the leaves
        # in search of the right place to insert
        while x != self.LEAF:
            y = x
            if insertion_node_value < x.value:
                x = x.left
            else:
                x = x.right

        # set parent for insertion node
        # to check if the top of the tree exists
        insertion_node.parent = y

        if y is None:
            self.root = insertion_node
        elif insertion_node.value < y.value:
            y.left = insertion_node
        else:
            y.right = insertion_node

        # insertion_node like current node or N
        # case 1
        if insertion_node is self.root:
            self.insert_case1(insertion_node)
        # case 2
        elif insertion_node.parent.color == NodeColor.BLACK:
            self.insert_case2(insertion_node)
        # case 3 - insertion_node parent is red
        elif Node.get_uncle(insertion_node).color == NodeColor.RED:
            self.insert_case3(insertion_node)
        elif insertion_node.parent.right == insertion_node and Node.get_grandparent(
                insertion_node).left == insertion_node.parent \
                or insertion_node.parent.left == insertion_node and Node.get_grandparent(
            insertion_node).right == insertion_node.parent:
            self.insert_case4(insertion_node)
        elif insertion_node.parent == NodeColor.RED and Node.get_grandparent(insertion_node).left == NodeColor.BLACK \
                and insertion_node.parent.left == insertion_node and Node.get_grandparent(
            insertion_node).left == insertion_node.parent \
                or insertion_node.parent == NodeColor.RED and Node.get_grandparent(
            insertion_node).right == NodeColor.BLACK \
                and insertion_node.parent.right == insertion_node and Node.get_grandparent(
            insertion_node).right == insertion_node.parent:
            self.insert_case5(insertion_node)

    def print_postorder_tree_view(self, node):
        if node:
            self.print_postorder_tree_view(node.left)
            self.print_postorder_tree_view(node.right)
            print("{0} - {0}".format(node.value, node.value.color), end="  ")

    def insert_case1(self, current_node):
        if current_node.parent is None:
            current_node.color = NodeColor.BLACK
        else:
            self.insert_case2(current_node)

    def insert_case2(self, current_node):
        if current_node.parent.color == NodeColor.BLACK:
            return
        else:
            self.insert_case3(current_node)

    def insert_case3(self, current_node):
        if Node.get_uncle(current_node) is not self.LEAF:
            current_node.parent.color = NodeColor.BLACK
            Node.get_uncle(current_node).color = NodeColor.BLACK
            Node.get_grandparent(current_node).color = NodeColor.RED
            self.insert_case1(Node.get_grandparent(current_node))
        else:
            self.insert_case4(current_node)

    def insert_case4(self, current_node):
        if current_node.parent.right == current_node and Node.get_grandparent(current_node).left == current_node.parent:
            self.left_rotate(current_node.parent)
            current_node = current_node.left
        elif current_node.parent.left == current_node and Node.get_grandparent(
                current_node).right == current_node.parent:
            self.right_rotate(current_node.parent)
            current_node = current_node.right
        self.insert_case5(current_node)

    def insert_case5(self, current_node):
        if current_node.parent == NodeColor.RED and Node.get_grandparent(current_node).left == NodeColor.BLACK \
                and current_node.parent.left == current_node \
                and Node.get_grandparent(current_node).left == current_node.parent:
            self.right_rotate(Node.get_grandparent(current_node))
        else:
            self.left_rotate(Node.get_grandparent(current_node))
