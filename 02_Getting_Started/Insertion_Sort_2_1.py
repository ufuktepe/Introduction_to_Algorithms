def insertion_sort(lst):
    # Iterate over the list starting from the 2nd item
    for j in range(1, len(lst)):
        # Get the current item
        key = lst[j]

        # Insert key into the sorted sequence lst[:j - 1]
        i = j - 1

        # Compare the key going backwards from j - 1
        while i >= 0 and key < lst[i]:
            # If key is smaller than lst[i] set lst[i + 1] to lst[i]
            lst[i + 1] = lst[i]
            i = i - 1
        lst[i + 1] = key

    return lst


print(insertion_sort([5, 2, 4, 6, 1, 3]))



