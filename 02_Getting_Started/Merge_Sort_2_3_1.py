def merge_sort(lst):

    # Return the list if it only has a single item
    if len(lst) == 1:
        return lst

    # Integer divide to find the mid of the list
    mid = len(lst) // 2

    # Create the left and right lists
    left = lst[:mid]
    right = lst[mid:]

    # Sort the lists
    merge_sort(left)
    merge_sort(right)

    i = 0
    j = 0
    k = 0

    # Merge the left and right lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    # Check if any item was left
    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1


sample = [2, 4, 3, 7, 1, 5, 8]
merge_sort(sample)
print(sample)
