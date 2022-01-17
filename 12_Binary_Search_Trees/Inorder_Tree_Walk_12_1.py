def inorder_tree_walk(lst, i):
    """
    Recursively traverses the binary tree (lst) and prints the items in ascending order
    :param lst: array (binary tree)
    :param i: index of the parent node
    :return: None
    """

    # Index of left child
    left = 2 * i + 1

    # index of right child
    right = 2 * i + 2

    # Traverse the left tree
    if left < len(lst):
        inorder_tree_walk(lst, left)

    # Print the parent
    print(lst[i])

    # Traverse the right tree
    if right < len(lst):
        inorder_tree_walk(lst, right)


if __name__ == '__main__':
    sample = [6, 4, 7, 2, 5, 6, 8]

    inorder_tree_walk(sample, 0)


