
def merge_sort_recursive(lst):
    """
    Recursively sorts the list by dividing the list into 2 halves and merging them.
    :param lst: input list
    :return: None
    """
    if len(lst) == 1:
        return lst

    left = lst[:len(lst)//2]
    right = lst[len(lst)//2:]

    merge_sort_recursive(left)
    merge_sort_recursive(right)
    merge_iterative_inplace(left, right, lst)


def merge_iterative_inplace(a, b, lst):
    """
    Merges two already sorted lists in place. Keeps track of indices i and j and increments them as elements are added to the
    main list.
    :param a: first list to be merged
    :param b: second list to be merged
    :param lst: main list
    :return: None
    """

    i = 0
    j = 0
    k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            lst[k] = a[i]
            i += 1
        else:
            lst[k] = b[j]
            j += 1
        k += 1

    # Get the rest of the items
    while i < len(a):
        lst[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        lst[k] = b[j]
        j += 1
        k += 1


def merge_sort_iterative(lst):
    """
    Iteratively sorts a list. First creates a main list of single element lists and iteratively pops the first 2
    elements in the main list merges them and adds the merged list at the end of the main list
    :param lst: input list
    :return: sorted list
    """

    # Create the main list
    q = []

    # Create a list of single element lists
    for n in lst:
        q.append([n])

    count = 1
    while len(q) > 1:
        # Pop the first 2 elements of q, merge them, and then add the merged list at the end of q

        # # Merge q.pop(0), q.pop(0) iteratively
        # q.append(merge_iterative(q.pop(0), q.pop(0)))

        # Merge q.pop(0), q.pop(0) recursively
        q.append(merge_recursive(q.pop(0), q.pop(0)))
        print(count)
        count += 1

    if q:
        return q[0]
    return []


def merge_iterative(a, b):
    """
    Merges two already sorted lists. Keeps track of indices i and j and increments them as elements are added to the
    merged list.
    :param a: first list to be merged
    :param b: second list to be merged
    :return: merged list
    """
    res = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    # Get the rest of the items
    while i < len(a):
        res.append(a[i])
        i += 1
    while j < len(b):
        res.append(b[j])
        j += 1

    return res


def merge_recursive(a, b):
    """
    Recursively merges two already sorted lists.
    :param a: first list to be merged
    :param b: second list to be merged
    :return: merged list
    """

    # If one of the lists is empty return the other list
    if not a:
        return b
    if not b:
        return a

    res = []

    # Add the smallest item to list u
    if a[0] < b[0]:
        res.append(a.pop(0))
    else:
        res.append(b.pop(0))

    # Recursively extend the list
    res.extend(merge_recursive(a, b))

    return res


if __name__ == '__main__':
    lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

    # # Iterative approach
    # print(merge_sort_iterative(lst))

    # Recursive approach
    merge_sort_recursive(lst)
    print(lst)