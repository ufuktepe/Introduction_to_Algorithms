class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def add_child(self, node):
        if node is None:
            return

        if node.key < self.key:
            self.left = node
        else:
            self.right = node

        node.parent = self

    def add_left_child(self, node):
        self.left = node
        if node is not None:
            node.parent = self

    def add_right_child(self, node):
        self.right = node
        if node is not None:
            node.parent = self

    def __str__(self):
        node_str = f'key:{self.key}'
        if self.left is not None:
            node_str += f' left:{self.left.key}'
        else:
            node_str += f' left:NA'

        if self.right is not None:
            node_str += f' right:{self.right.key}'
        else:
            node_str += f' right:NA'

        return node_str


class Tree:
    def __init__(self, root):
        self.root = root

    def print_nodes(self, root):
        """
        Prints the nodes of the subtree rooted at the given root
        :param root: root of the subtree
        :return: None
        """
        if root is None:
            return

        self.print_nodes(root.left)
        print(root)
        self.print_nodes(root.right)


def tree_insert(root, val):
    """
    Inserts a value into a tree. The new node will be a leaf.
    :param root: root node of the tree
    :param val: value to be inserted
    :return: None
    """

    # Create the new node
    new_node = Node(val)
    x = root
    parent = None

    # Traverse the tree from the root down to a leaf which has an empty spot for a child (new node).
    while x is not None:
        parent = x

        if val < x.key:
            x = x.left
        else:
            x = x.right

    # If the tree was not empty, the parent has an empty spot for the new node
    if parent is not None:
        parent.add_child(new_node)
    else:
        print('The tree was empty')


def tree_delete(T, z):
    """
    Deletes z from the tree. There are 4 cases:
    Case 1: z has no left child
    Case 2: z has a left child but no right child
    Case 3: z has both children and y (z's successor) is z's right child
    Case 4: z has both children and y (z's successor) is not z's right child
    :param T: the given tree
    :param z: node to be removed
    :return: None
    """
    if z.left is None:
        # Case 1: z has no left child. The right subtree becomes the new tree.
        transplant(T, z, z.right)
    elif z.right is None:
        # Case 2: z has a left child but no right child. The left subtree becomes the new tree.
        transplant(T, z, z.left)
    else:
        # Get the successor of z (y should not have a left child since it is the successor of z)
        y = tree_minimum(z.right)

        if y.parent != z:
            # Case 4: y is not z's right child.
            # Replace the subtree rooted at y with the subtree rooted at y.right (connects y's parent with y.right)
            transplant(T, y, y.right)
            # Set y.right to z.right (y's right child becomes z's right child)
            y.add_right_child(z.right)
        # Case 3 and 4:
        # Replace the subtree rooted at z with the subtree rooted at y (connect z's parent with y)
        transplant(T, z, y)
        # Set y.left to z.left
        y.add_left_child(z.left)


def tree_minimum(node):
    if node.left is None:
        return node
    return tree_minimum(node.left)


def transplant(T, u, v):
    """
    Replaces the subtree rooted at u with the subtree rooted at v.
    :param T: the given tree
    :param u: root of the subtree to be replaced with the subtree rooted at v
    :param v: root of the subtree to replace the subtree rooted at u
    :return: None
    """
    if u.parent is None:
        T.root = v
    elif u == u.parent.left:
        u.parent.add_left_child(v)
    else:
        u.parent.add_right_child(v)


if __name__ == '__main__':
    # The below tree can be found in Chp 12.3 of CLRS
    n1 = Node(12)
    n2 = Node(5)
    n3 = Node(18)
    n4 = Node(2)
    n5 = Node(9)
    n6 = Node(15)
    n7 = Node(19)
    n8 = Node(17)

    n1.add_child(n2)
    n1.add_child(n3)
    n2.add_child(n4)
    n2.add_child(n5)
    n3.add_child(n6)
    n3.add_child(n7)
    n6.add_child(n8)

    nodes_set = {n1, n2, n3, n4, n5, n6, n7, n8}

    # # Example for insert
    # tree_insert(n1, 13)
    #
    # for n in nodes_set:
    #     print(n)

    # # Example for finding the minimum
    # print(tree_minimum(n1))

    # Example for deletion
    tree = Tree(n1)
    print('\nBefore deletion')
    tree.print_nodes(tree.root)
    print('\nAfter deletion')

    tree_delete(tree, n1)
    tree.print_nodes(tree.root)




