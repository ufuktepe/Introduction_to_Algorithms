def min_heapify(lst, i):
    """
    Assumes the left and right child binary trees of lst[i] are min-heaps.
    Floats down the value at lst[i] to its correct position so that the subtree rooted at index i obeys the min heap
    property.
    Time complexity: O(log n)
    :param lst: input array
    :param i: index of the item to be positioned
    :return: None
    """

    left = 2 * i + 1
    right = 2 * i + 2

    heap_size = len(lst)

    # Check if the left node is smaller than the current node
    if heap_size > left and lst[left] < lst[i]:
        min_idx = left
    else:
        min_idx = i

    # Check if the right node is smaller than the lst[min_idx]
    if heap_size > right and lst[right] < lst[min_idx]:
        min_idx = right

    # If lst[i] is not the min, swap lst[min_idx] with lst[i] and call min_heapify again
    if min_idx != i:
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        min_heapify(lst, min_idx)


def build_min_heap(lst):
    """
    Builds a min-heap
    Time complexity: O(n)
    :param lst: input array
    :return: None
    """
    for i in range(len(lst) // 2, -1, -1):
        min_heapify(lst, i)


def extract_min(lst):
    """
    Removes and returns the item with the minimum key (lst[0]).
    :param lst: input array
    :return: item with the smallest key
    """

    if len(lst) < 1:
        raise IndexError()

    min = lst[0]

    # Replace the first item with the last item
    lst[0] = lst[-1]

    # Remove the last item
    del lst[-1]

    # Restore the min heap property
    build_min_heap(lst)

    return min


def restore_min_heap_property(lst, i):
    """
    Finds the correct position for lst[i] by traversing the tree from i to the root.
    Recursively compares the value of the child node to its parent and swaps the child and parent if child has smaller
    value.
    :param lst: input array
    :param i: index of the child node
    :return: none
    """

    if i == 0:
        return

    parent_idx = (i - 1) // 2

    if lst[parent_idx] > lst[i]:
        # Swap the parent with the child
        lst[i], lst[parent_idx] = lst[parent_idx], lst[i]
        # Check if the position of lst[parent_idx] is correct
        restore_min_heap_property(lst, parent_idx)


def min_heap_insert(lst, node):
    """
    Inserts a node to a min heap.
    :param lst: input array (min heap)
    :param node: node to be inserted in the min heap
    :return: None
    """
    lst.append(node)
    restore_min_heap_property(lst, len(lst) - 1)


def heap_decrease_key(lst, i, key):
    """
    Sets the value of lst[i] to key and calls restore_min_heap_property to find the correct position for the value of
    lst[i].
    :param lst: input array
    :param i: index of the item whose value will be updated
    :param key: new value for lst[i]
    :return: None
    """

    # Check if the new value is larger than the current value
    if key > lst[i]:
        print('new key is larger than current key.')
        return

    # Update the value of lst[i] to its new value
    lst[i] = key

    # Restore the min-heap property
    restore_min_heap_property(lst, i)
