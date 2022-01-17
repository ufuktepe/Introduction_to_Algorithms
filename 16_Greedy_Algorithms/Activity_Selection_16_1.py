from Activity_Selection_From_Chp_16 import Activity


def recursive_activity_selector(a, idx, output_list):
    """
    Recursively finds the max set of compatible activities from a given list of activities.
    :param a: list of activities sorted in increasing finishing time
    :param idx: starting index of the sub-problem to be solved
    :param output_list: list including the max set of compatible activities
    :return: output_list
    """
    # if idx is equal to te length that means we have examined all activities
    if idx == len(a):
        return output_list

    # Add the current idx to the list
    output_list.append(idx)

    # Find the next compatible index
    next_idx = idx + 1
    while next_idx < len(a) and not (a[idx].is_compatible(a[next_idx])):
        next_idx += 1

    # Return the list
    return recursive_activity_selector(a, next_idx, output_list)


def activity_selector(a):
    """
    Iteratively finds the max set of compatible activities from a given list of activities.
    :param a: list of activities sorted in increasing finishing time
    :return: output_list
    """

    # Add the first index of the activity since its finishing time is less than other activities' finishing times
    output_list = [0]

    curr_idx = 0

    # Iteratively find next compatible activities and add their indices to the output_list and update the curr_idx
    # along the way
    for i in range(1, len(a)):
        if a[curr_idx].is_compatible(a[i]):
            output_list.append(i)
            curr_idx = i

    return output_list


if __name__ == '__main__':
    start_times = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    finish_times = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

    # start_times = [1, 3, 5, 11, 13]
    # finish_times = [4, 8, 12, 14, 14]

    activities = list()

    for i in range(len(start_times)):
        activities.append(Activity(start_times[i], finish_times[i]))

    # # Example for the recursive approach
    # print(recursive_activity_selector(activities, 0, []))

    # Example for the iterative approach
    print(activity_selector(activities))

