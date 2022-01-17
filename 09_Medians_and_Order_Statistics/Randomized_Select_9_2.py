from Quicksort_7_1 import Quicksort


def randomized_select(lst, p, r, i):
    """
    Finds the ith smallest item in an array.
    @param lst: given array
    @param p: starting index
    @param r: ending index
    @param i: rank (i.e. 3 indicates the 3rd smallest item in the given array)
    @return: value of the ith smallest item in the array.
    """
    if p == r:
        return lst[p]

    # Partition the array
    q = Quicksort.partition(lst, p, r)

    # Find the local rank (q is the global index whereas k is the rank between p and r)
    k = q - p + 1

    if i == k:
        return lst[q]
    elif i < k:
        # Recurse in the first part
        return randomized_select(lst, p, q - 1, i)
    else:
        # Subtract k from i to get the local rank and recurse in the  2nd part
        return randomized_select(lst, q + 1, r, i - k)


sample = [2, 5, 3, 4, 1, 7, 6, 8]

answer = randomized_select(sample, 0, len(sample) - 1, 4)
print(answer)
