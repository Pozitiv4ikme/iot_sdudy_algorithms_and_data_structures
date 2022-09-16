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



class NodeColor(Enum):
    RED = 'red_node'
    BLACK = 'black_node'
