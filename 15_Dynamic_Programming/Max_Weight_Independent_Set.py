def max_wis_bottom_up(lst):
    """
    Finds the value of maximum weight independent set of a given array using a bottom-up fashion.
    :param lst: the given input array
    :return: value of the maximum weight independent set
    """

    # Initialize the output list.
    # output_lst[i] is the value of the max weight independent set in the array [0, 1, ..., i]
    output_lst = [None for i in range(len(lst))]

    # Populate the first item of the output list
    output_lst[0] = lst[0]

    # Populate the second item of the output list. output_lst[1] = max(lst[0], lst[1])
    if lst[0] > lst[1]:
        output_lst[1] = lst[0]
    else:
        output_lst[1] = lst[1]

    # Populate output_lst starting from output_lst[2]
    for i in range(2, len(lst)):

        x = output_lst[i - 1]
        y = output_lst[i - 2] + lst[i]

        if y > x:
            output_lst[i] = y
        else:
            output_lst[i] = x

    return output_lst[len(lst) - 1]


def max_wis_recursive(lst, last_idx, output_lst):
    """
    Finds the value of maximum weight independent set of a given array using recursion.
    :param lst: the given input array
    :param last_idx: last index to be considered in lst
    :param output_lst: list containing the value of max weight independent set for each sub-problem.
    For example output_lst[i] is the value of the max weight independent set in the array [0, 1, ..., i]
    :return: value of the maximum weight independent set
    """

    # Return 0 if last_idx is negative
    if last_idx < 0:
        return 0

    # Check if the solution for sub-problem output_lst[last_idx - 1] already exists. If it doesn't exist, recursively
    # find the solution.
    if output_lst[last_idx - 1] is not None:
        x = output_lst[last_idx - 1]
    else:
        x = max_wis_recursive(lst, last_idx - 1, output_lst)

    # Check if the solution for sub-problem output_lst[last_idx - 2] already exists. If it doesn't exist, recursively
    # find the solution.
    if output_lst[last_idx - 2] is not None:
        y = output_lst[last_idx - 2]
    else:
        y = max_wis_recursive(lst, last_idx - 2, output_lst)

    # Populate output_lst[last_idx]
    if y + lst[last_idx] > x:
        output_lst[last_idx] = y + lst[last_idx]
    else:
        output_lst[last_idx] = x

    return output_lst[last_idx]


if __name__ == '__main__':
    lst = [3, 100, 4, 1, 101, 100, 6]

    # # Example for max_wis_recursive
    # output_lst = [None for i in range(len(lst))]
    # m = max_wis_recursive(lst, len(lst) - 1, output_lst)
    # print(m)

    # Example for max_wis_bottom_up
    print(max_wis_bottom_up(lst))