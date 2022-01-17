import sys
from Max_Heapify_6_2 import *


def heap_extract_max(lst):
    """
    Removes and returns the item with the largest key (lst[0]).
    :param lst: input array
    :return: item with the largest key
    """

    if len(lst) < 1:
        raise IndexError()

    max = lst[0]

    # Replace the first item with the last item
    lst[0] = lst[-1]

    # Remove the last item
    del lst[-1]

    # Restore the max heap property
    max_heapify(lst, 0, len(lst))

    return max


def heap_increase_key(lst, i, key):
    """
    Sets the value of lst[i] to key and calls restore_max_heap_property to find the correct position for the value
    of lst[i]
    :param lst: input array
    :param i: index of the item whose value will be updated
    :param key: new value for lst[i]
    :return: None
    """

    # Check if the new value is smaller than the current value
    if key < lst[i]:
        print('new key is smaller than current key.')
        return

    # Update the value of lst[i] to its new value
    lst[i] = key

    # Restore the max-heap property
    restore_max_heap_property(lst, i)


def restore_max_heap_property(lst, i):
    """
    Traverses a path from a node toward the root to find a proper place for lst[i].
    Recursively compares the value of the child node to its parent and swaps the child and parent if child has larger
    value.
    :param lst: input array
    :param i: index of the child node
    :return: None
    """
    if i == 0:
        return

    parent_idx = (i - 1) // 2
    if lst[parent_idx] < lst[i]:
        # Swap the parent with the child
        lst[i], lst[parent_idx] = lst[parent_idx], lst[i]
        # Check if the position of lst[parent_idx] is correct
        restore_max_heap_property(lst, parent_idx)


def max_heap_insert(lst, key):
    """
    Appends negative infinity to the list and then calls heap_increase_key to update its value to key.
    :param lst: input array
    :param key: value of the new node
    :return: None
    """
    lst.append(float('-inf'))
    heap_increase_key(lst, len(lst) - 1, key)


if __name__ == '__main__':
    sample = [3, 9, 2, 4, 6]
    build_max_heap(sample)
    print(sample)

    # # Example for heap_extract_max
    # heap_size = len(sample)
    # for i in range(heap_size):
    #     print(heap_extract_max(sample))

    # # Example for heap_increase_key
    # heap_increase_key(sample, 4, 7)
    # print(sample)

    # Example for max_heap_insert
    max_heap_insert(sample, 7)
    print(sample)
