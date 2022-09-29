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
        y.parent = node.parent

        # find the side of x by his parent and put here y
        # it is like node swap and make y like root
        if node.parent is not self.LEAF:
            node.parent.right = y
        else:
            node.parent.left = y

        # second step
        node.right = y.left

        # fourth step
        y.left = node

    def right_rotate(self, node):
        y = node.left

        y.parent = node.parent
        if node.parent is not self.LEAF:
            node.parent.left = y
        else:
            node.parent.right = y

        node.left = y.right

        y.right = node

    # insert node
    def insert_node(self, insertion_node_value):

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
        elif Node.get_uncle(insertion_node) is not self.LEAF and Node.get_uncle(insertion_node).color == NodeColor.RED:
            self.insert_case3(insertion_node)

        # case 4
        elif (insertion_node.parent.right == insertion_node and Node.get_grandparent(insertion_node).left) == insertion_node.parent\
                or (insertion_node.parent.left == insertion_node and Node.get_grandparent(insertion_node).right) == insertion_node.parent:
            self.insert_case4(insertion_node)

        # case 5
        elif (insertion_node == insertion_node.parent.left and insertion_node.parent == Node.get_grandparent(insertion_node).left and insertion_node.parent.color == NodeColor.RED and Node.get_grandparent(insertion_node).color == NodeColor.BLACK) \
                or (insertion_node == insertion_node.parent.right and insertion_node.parent == Node.get_grandparent(insertion_node).right and insertion_node.parent.color == NodeColor.RED and Node.get_grandparent(insertion_node).color == NodeColor.BLACK):
            self.insert_case5(insertion_node)

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
        if Node.get_uncle(current_node).color == NodeColor.RED:
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

        elif current_node.parent.left == current_node and Node.get_grandparent(current_node).right == current_node.parent:
            self.right_rotate(current_node.parent)
            current_node = current_node.right
        self.insert_case5(current_node)

    def insert_case5(self, current_node):
        current_node.parent.color = NodeColor.BLACK
        Node.get_grandparent(current_node).color = NodeColor.RED

        if current_node == current_node.parent.left and current_node.parent == Node.get_grandparent(current_node).left:
            self.right_rotate(Node.get_grandparent(current_node))
        else:
            self.left_rotate(Node.get_grandparent(current_node))

    def delete_node(self, node_value_to_delete):
        node_to_delete = self.LEAF
        tree = self.root

        # traversing the tree to the leaves
        # in search of the right place to delete
        while tree is not None:
            if node_value_to_delete == tree.value:
                node_to_delete = tree

            if tree.value <= node_value_to_delete:
                tree = tree.right
            else:
                tree = tree.left

        if node_to_delete == self.LEAF:
            print("Cannot find node with this value in the tree")
            return

        node_to_delete_brother = Node.get_sibling(node_to_delete)

        # case with one child
        if node_to_delete.right is self.LEAF or node_to_delete.left is self.LEAF:
            self.delete_one_child(node_to_delete)

        # case 1
        if node_to_delete.parent is not None:
            self.delete_case2(node_to_delete)

        # case 2
        elif node_to_delete_brother.color == NodeColor.RED:
            self.delete_case2(node_to_delete)

        # case 3
        elif node_to_delete_brother.color == NodeColor.BLACK:
            self.delete_case3(node_to_delete)

        # case 4
        elif node_to_delete.parent.color == NodeColor.RED and node_to_delete_brother.color == NodeColor.BLACK \
                and node_to_delete_brother.left.color == NodeColor.BLACK \
                and node_to_delete_brother.right.color == NodeColor.BLACK:
            self.delete_case4(node_to_delete)

        # case 5
        elif node_to_delete_brother.color == NodeColor.BLACK:
            self.delete_case5(node_to_delete)

        # case 6
        elif node_to_delete.parent.left == node_to_delete or node_to_delete.parent.right == node_to_delete:
            self.delete_case6(node_to_delete)

    def delete_one_child(self, node):
        # find not None child to copy
        if node.right is self.LEAF:
            child = node.left
        else:
            child = node.right
        Node.replace_child(node, child)
        if node.color == NodeColor.BLACK:
            if child.color == NodeColor.RED:
                child.color = NodeColor.BLACK
            else:
                self.delete_case1(child)

    def delete_case1(self, node_to_delete):
        if node_to_delete.parent is not None:
            self.delete_case2(node_to_delete)

    def delete_case2(self, node_to_delete):
        brother = Node.get_sibling(node_to_delete)

        if brother.color == NodeColor.RED:
            brother.parent.color = NodeColor.RED
            brother.color = NodeColor.BLACK

            if node_to_delete == node_to_delete.parent.left:
                self.left_rotate(node_to_delete.parent)
            else:
                self.right_rotate(node_to_delete.parent)
        else:
            self.delete_case3(node_to_delete)

    def delete_case3(self, node_to_delete):
        brother = Node.get_sibling(node_to_delete)

        if node_to_delete.parent.color == NodeColor.BLACK and brother.color == NodeColor.BLACK \
                and brother.left.color == NodeColor.BLACK and brother.right.color == NodeColor.BLACK:
            brother.color = NodeColor.RED
            self.delete_case1(node_to_delete.parent)
        else:
            self.delete_case4(node_to_delete)

    def delete_case4(self, node_to_delete):
        brother = Node.get_sibling(node_to_delete)

        if node_to_delete.parent.color == NodeColor.RED and brother.color == NodeColor.BLACK \
                and brother.left.color == NodeColor.BLACK and brother.right.color == NodeColor.BLACK:
            brother.color = NodeColor.RED
            node_to_delete.parent.color = NodeColor.BLACK
        else:
            self.delete_case5(node_to_delete)

    def delete_case5(self, node_to_delete):
        brother = Node.get_sibling(node_to_delete)

        if brother.color == NodeColor.BLACK:
            if node_to_delete == node_to_delete.parent.left and brother.right.color == NodeColor.BLACK \
                    and brother.left.color == NodeColor.RED:
                brother.color = NodeColor.RED
                brother.left.color = NodeColor.BLACK
                self.right_rotate(brother)
            elif node_to_delete == node_to_delete.parent.right and brother.left.color == NodeColor.BLACK \
                    and brother.right.color == NodeColor.RED:
                brother.color = NodeColor.BLACK
                brother.right.color = NodeColor.RED
                self.left_rotate(brother)
        else:
            self.delete_case6(node_to_delete)

    def delete_case6(self, node_to_delete):
        brother = Node.get_sibling(node_to_delete)

        brother.color = node_to_delete.parent.color
        node_to_delete.parent.color = NodeColor.BLACK

        if node_to_delete == node_to_delete.parent.left:
            brother.right.color = NodeColor.BLACK
            self.left_rotate(node_to_delete.parent)
        else:
            brother.left.color = NodeColor.BLACK
            self.right_rotate(node_to_delete.parent)
