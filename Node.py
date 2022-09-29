from enum import Enum


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.right = None
        self.left = None
        self.color = NodeColor.RED

    @staticmethod
    def get_grandparent(node):
        if node is not None and node.parent is not None:
            return node.parent.parent
        else:
            return None

    @staticmethod
    def get_uncle(node):
        node_grandparent = Node.get_grandparent(node)
        if not node_grandparent:
            return None
        elif Node.get_grandparent(node).right == node.parent:
            return node_grandparent.left
        else:
            return node_grandparent.right

    @staticmethod
    def get_sibling(node):
        if node.parent.left == node:
            return node.parent.right
        else:
            return node.parent.left

    @staticmethod
    def replace_child(node, child):
        # when the node needs to be removed, the children should remain as leaves
        child.parent = node.parent

        if node == node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child


class NodeColor(Enum):
    RED = 'red_node'
    BLACK = 'black_node'
