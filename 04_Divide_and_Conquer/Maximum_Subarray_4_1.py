"""
Finds a subarray crossing the midpoint of the given array whose sum of values is the maximum among all subarrays that
are crossing the midpoint of the given array.
lst: input array
"""
def find_max_crossing_subarray(lst, low, mid, high):
    if high - low == 0:
        raise Exception('Invalid input!')
    elif high - low == 1:
        return low, high, lst[low] + lst[high]

    left_sum = None
    sum = 0
    left_index = mid

    for i in range(mid, low - 1, -1):
        sum += lst[i]

        # Check if sum is larger than or equal to left_sum
        if left_sum is None or sum >= left_sum:
            left_sum = sum
            # Update the index
            left_index = i

    right_sum = None
    sum = 0
    right_index = mid + 1

    for i in range(mid + 1, high + 1):
        sum += lst[i]

        # Check if sum is larger than or equal to right_sum
        if right_sum is None or sum >= right_sum:
            right_sum = sum
            # Update the index
            right_index = i

    return left_index, right_index, left_sum + right_sum


def find_max_subarray(lst, low, high):
    """
    Finds a subarray whose sum of values is the maximum among all subarrays of a given array starting from index low
    to index high.
    @param lst: given array
    @param low: starting index
    @param high: ending index
    @return: tuple that includes the start index, end index and the sum of values of the maximum subarray
    """
    if len(lst[low:high + 1]) == 1:
        return low, high, lst[low]

    mid = (high + low) // 2

    # Find the max subarray in the left half
    left_start, left_end, left_sum = find_max_subarray(lst, low, mid)

    # Find the max subarray in the right half
    right_start, right_end, right_sum = find_max_subarray(lst, mid + 1, high)

    # Find the max crossing subarray
    cross_start, cross_end, cross_sum = find_max_crossing_subarray(lst, low, mid, high)

    # Find the max among the 3 results
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_start, left_end, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_start, right_end, right_sum
    else:
        return cross_start, cross_end, cross_sum


sample = [1, 3, -3, -1]

start, end, sum = find_max_subarray(sample, 0, len(sample) - 1)

print(start)
print(end)
print(sum)




