def tree_search(lst, i, val):
    """
    Recursively searches for the given value in the binary tree. Returns the index of the value if the value exists.
    Otherwise, returns none.
    :param lst: input array (binary tree)
    :param i: index of the parent node
    :param val: searched value
    :return: index of the value or None
    """

    # Return None if i is out of bounds
    if i >= len(lst):
        return None

    # Index of left child
    left = 2 * i + 1

    # index of right child
    right = 2 * i + 2

    if val == lst[i]:
        # Return the index of the value
        return i

    if val < lst[i]:
        # Recurse in the left tree
        return tree_search(lst, left, val)
    else:
        # Recurse in the right tree
        return tree_search(lst, right, val)


def tree_minimum(lst, i):
    """
    Finds the min item in a binary tree by traversing the left tree of each node.
    :param lst: input array (binary tree)
    :param i: index of the parent node
    :return: min item in the binary tree
    """
    # Index of left child
    left = 2 * i + 1

    if left >= len(lst):
        return lst[i]

    return tree_minimum(lst, left)


def tree_maximum(lst, i):
    """
    Finds the max item in a binary tree by traversing the right tree of each node.
    :param lst: input array (binary tree)
    :param i: index of the parent node
    :return: max item in the binary tree
    """
    # Index of right child
    right = 2 * i + 2

    if right >= len(lst):
        return lst[i]

    return tree_maximum(lst, right)


def tree_successor(lst, i):
    """
    Returns the successor of a node.
    :param lst: input array (binary tree)
    :param i: index of the parent node
    :return: successor of the given node
    """

    # index of right child
    right = 2 * i + 2

    # If the right tree is non-empty, return the min node of the right tree
    if right < len(lst):
        return tree_minimum(lst, right)

    # If the right tree is empty, return the lowest ancestor of lst[i] whose left child is also an ancestor of lst[i]
    parent = (i - 1) // 2
    child = i

    # Check if it has a parent
    if parent < 0:
        return 'No successor found'

    while lst[parent] < lst[child]:
        child = parent
        parent = (child - 1) // 2

        if parent < 0:
            return 'No successor found'

    return lst[parent]


if __name__ == '__main__':
    sample = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]

    # print(tree_search(sample, 0, 9))

    # print(tree_minimum(sample, 0))
    # print(tree_maximum(sample, 0))

    print(tree_successor(sample, 3))
