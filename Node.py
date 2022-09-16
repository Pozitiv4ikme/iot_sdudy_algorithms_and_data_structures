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
        grandparent_node = Node.get_grandparent(node)
        if node is not None and grandparent_node is not None:
            return grandparent_node.right


class NodeColor(Enum):
    RED = 'red_node'
    BLACK = 'black_node'
