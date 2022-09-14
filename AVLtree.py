from Node import Node


def insert(root_node: Node, insertion_node_value):
    if not root_node:  # if you forget to create root - first insert becomes root
        return Node(insertion_node_value)
    elif root_node.value == insertion_node_value:  # you cannot insert a node that already exists in the tree
        return root_node
    elif root_node.value > insertion_node_value:  # go to the left or right subtree in search of the desired node
        root_node.left = insert(root_node.left, insertion_node_value)
    else:
        root_node.right = insert(root_node.right, insertion_node_value)

    # increase height for parent node
    root_node.height = 1 + max(getNodeHeight(root_node.left), getNodeHeight(root_node.right))

    # count balance factor for parent node
    balance_factor = nodeBalance(root_node)

    # cases for maintenance of AVL tree rules: balance factor for all nodes 1|-1 and leafs 0
    # left-left case
    if balance_factor > 1 and insertion_node_value < root_node.value:
        return rightRotate(root_node)

    # left-right case
    if balance_factor > 1 and insertion_node_value > root_node.value:
        root_node.left = leftRotate(root_node.left)
        return rightRotate(root_node)

    # right-right case
    if balance_factor < -1 and insertion_node_value > root_node.value:
        return leftRotate(root_node)

    # right-left case
    if balance_factor < -1 and insertion_node_value < root_node.value:
        root_node.right = rightRotate(root_node.right)
        return leftRotate(root_node)

    return root_node


def deleteNode(tree_root_node: Node, deletion_node_value):
    if not tree_root_node:
        return tree_root_node

    elif tree_root_node.value > deletion_node_value:  # go to the left or right subtree in search of the desired node
        tree_root_node.left = deleteNode(tree_root_node.left, deletion_node_value)

    elif tree_root_node.value < deletion_node_value:
        tree_root_node.right = deleteNode(tree_root_node.right, deletion_node_value)

    # one child case
    else:
        if not tree_root_node.left:  # when no child in left subtree
            temp = tree_root_node.right  # swap right and current node
            root_node = None
            return temp

        elif not tree_root_node.right:
            temp = tree_root_node.left
            root_node = None
            return temp

        # two child case
        temp = treeMinValue(tree_root_node.right)  # find min element in right subtree, for copy subtree in future

        tree_root_node.value = temp.value  # this value assign to node root value

        tree_root_node.right = deleteNode(tree_root_node.right, temp.value)  # delete root node

    # after delete we must check if the balance is maintained
    if not tree_root_node:
        return tree_root_node

    # like case to insert, but
    tree_root_node.height = 1 + max(getNodeHeight(tree_root_node.left), getNodeHeight(tree_root_node.right))

    balance = nodeBalance(tree_root_node)

    if balance > 1 and nodeBalance(tree_root_node.left) >= 0:  # zero - tree leaf; getBalance(root.left) or
        return rightRotate(tree_root_node)  # getBalance(root.right) - check balance factor and

    if balance > 1 and nodeBalance(tree_root_node.left) < 0:  # determine which side prevails or for example
        tree_root_node.left = leftRotate(tree_root_node.left)  # in left subtree which case: left-left or left-right
        return rightRotate(tree_root_node)

    if balance < -1 and nodeBalance(tree_root_node.right) <= 0:
        return leftRotate(tree_root_node)

    if balance < -1 and nodeBalance(tree_root_node.right) < 0:
        tree_root_node.right = rightRotate(tree_root_node.right)
        return leftRotate(tree_root_node)

    return tree_root_node


def getNodeHeight(node):
    if not node:
        return 0
    return node.height


def nodeBalance(node):
    if not node:
        return 0
    return getNodeHeight(node.left) - getNodeHeight(node.right)


# Rotate which we use in insert/delete cases
def rightRotate(node):
    y = node.left
    x = y.right

    y.right = node
    node.left = x

    node.height = max(getNodeHeight(node.left), getNodeHeight(node.right))
    y.height = max(getNodeHeight(y.left), getNodeHeight(y.right))

    return y


def leftRotate(node):
    y = node.right
    x = y.left

    y.left = node
    node.right = x

    node.height = max(getNodeHeight(node.left), getNodeHeight(node.right))
    y.height = max(getNodeHeight(y.left), getNodeHeight(y.right))

    return y


def treeMinValue(node):
    if not node or not node.left:
        return node
    return treeMinValue(node.left)


def printInorderTreeView(tree_node):
    if tree_node:
        printInorderTreeView(tree_node.left)
        print("{0}".format(tree_node.value), end=" ")
        printInorderTreeView(tree_node.right)


def printPreorderTreeView(tree_node):
    if not tree_node:
        return
    print("{0} ".format(tree_node.value), end=" ")
    printPreorderTreeView(tree_node.left)
    printPreorderTreeView(tree_node.right)


def printPostorderTreeView(tree_node):
    if tree_node:
        printPostorderTreeView(tree_node.left)
        printPostorderTreeView(tree_node.right)
        print("{0}  ".format(tree_node.value), end=" ")
