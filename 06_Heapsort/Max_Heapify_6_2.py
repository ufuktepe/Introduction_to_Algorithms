def max_heapify(lst, i, heap_size):
    """
    Assumes the left and right child binary trees of lst[i] are max-heaps.
    Floats down the value at lst[i] to its correct position so that the subtree rooted at index i obeys the max heap
    property.
    Time complexity: O(log n)
    :param lst: input array
    :param i: index of the item to be positioned
    :param heap_size: the length of the array to be heapified starting from the beginning of the array.
    :return: None
    """

    # Get the left and right indices
    left_idx = 2 * i + 1
    right_idx = 2 * i + 2

    # Check if the left index has a larger value than lst[i]
    if heap_size > left_idx and lst[i] < lst[left_idx]:
        largest_idx = left_idx
    else:
        largest_idx = i

    # Check if the right index has a larger value than lst[largest_idx]
    if heap_size > right_idx and lst[largest_idx] < lst[right_idx]:
        largest_idx = right_idx

    # If lst[i] is not the largest, swap the largest value with lst[i] and call max_heapify again
    if largest_idx != i:
        lst[i], lst[largest_idx] = lst[largest_idx], lst[i]
        max_heapify(lst, largest_idx, heap_size)


def build_max_heap(lst):
    """
    Builds a max-heap (Chp 6.3 in CLRS)
    Time complexity: O(n)
    :param lst: input array
    :return: None
    """
    for pos in range(len(lst) // 2 - 1, -1, -1):
        max_heapify(lst, pos, len(lst))


if __name__ == '__main__':
    sample = [3, 9, 5, 8, 4, 6, 10]
    build_max_heap(sample)
    print(sample)