from Max_Heapify_6_2 import *


def heapsort(lst):
    """
    First builds a max-heap (O(n))
    Then decrements the heap-size one by one until the heap size is 2 and in each iteration calls max_heapify on the
    first item.
    Time  complexity: O(n log(n))
    :param lst: input array
    :return: None
    """
    # First build a max-heap
    build_max_heap(lst)
    heap_size = len(lst)

    while heap_size > 1:
        # Swap the first item with the last item
        lst[0], lst[heap_size - 1] = lst[heap_size - 1], lst[0]
        heap_size -= 1
        # The new root might violate the max-heap property. Restore the max-heap property
        max_heapify(lst, 0, heap_size)


if __name__ == '__main__':
    sample = [3, 9, 2, 5, 4, 6]
    heapsort(sample)
    print(sample)

