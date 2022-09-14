from Node import Node
from AVLtree import *


root_tree_node = None
# root_tree_node = Node(50)

root_tree_node = insert(root_tree_node, 50)
root_tree_node = insert(root_tree_node, 40)
root_tree_node = insert(root_tree_node, 30)

root_tree_node = insert(root_tree_node, 10)

root_tree_node = insert(root_tree_node, 10)
root_tree_node = insert(root_tree_node, 60)
root_tree_node = insert(root_tree_node, 70)
root_tree_node = insert(root_tree_node, 35)

print(" ")
print("Inorder tree view:")
printInorderTreeView(root_tree_node)
print(" ")

print(" ")
print("Preorder tree view:")
printPreorderTreeView(root_tree_node)
print(" ")

print(" ")
print("Before delete")
printPostorderTreeView(root_tree_node)
print(" ")

deleteNode(root_tree_node, 50)

print(" ")
print("After delete")
printPostorderTreeView(root_tree_node)
print(" ")
