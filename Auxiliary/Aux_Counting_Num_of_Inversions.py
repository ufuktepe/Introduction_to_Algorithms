def merge_and_count_split_inversions(lst_a, lst_b):
    """
    Counts the number of split inversions (inversions between sorted array lst_a and sorted array lst_b) and merges the
    two arrays. While doing the merging, when an item x gets copied from lst_b to the output_lst, this indicates the
    remaining items in lst_a are larger than x. So the number of inversions associated with item x is the number of
    remaining items in  lst_a.
    @param lst_a: first sorted array
    @param lst_b: second sorted array
    @return: sorted array and the number of split inversions
    """

    output_lst = list()

    i = 0
    j = 0
    num_of_split_inversions = 0

    while i < len(lst_a) and j < len(lst_b):
        if lst_a[i] < lst_b[j]:
            output_lst.append(lst_a[i])
            i += 1
        else:
            output_lst.append(lst_b[j])
            j += 1
            # Add the number of remaining items in lst_a
            num_of_split_inversions += len(lst_a) - i

    # Check for left items
    while i < len(lst_a):
        output_lst.append(lst_a[i])
        i += 1
    while j < len(lst_b):
        output_lst.append(lst_b[j])
        j += 1

    return output_lst, num_of_split_inversions


def sort_and_count(lst):
    """
    Counts the number of inversions in a given array.
    @param lst: given array
    @return: sorted array and the number of inversions
    """
    if len(lst) == 1:
        # Return the list which has zero inversions
        return lst, 0

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    # Sort the left array and get the number of inversions
    sorted_left, left_inversion_count = sort_and_count(left)

    # Sort the right array and get the number of inversions
    sorted_right, right_inversion_count = sort_and_count(right)

    # Merge and sort sorted_left and sorted_right, and get the number of split inversions
    sorted_and_merged, split_inversion_count = merge_and_count_split_inversions(sorted_left, sorted_right)

    return sorted_and_merged, left_inversion_count + right_inversion_count + split_inversion_count


sample = [1, 3, 5, 2, 4, 6]

sorted_lst, count = sort_and_count(sample)

print(count)