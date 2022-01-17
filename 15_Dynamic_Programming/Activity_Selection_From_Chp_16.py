from copy import deepcopy


class Activity:
    def __init__(self, s, f):
        # Starting time of the activity
        self.start = s
        # Finishing time of the activity
        self.finish = f

    def is_compatible(self, other_activity):
        # Returns true if the other_activity is compatible with this activity
        return self.start > other_activity.finish or self.finish < other_activity.start


def find_max_set_of_compatible_activities(a):
    """
    Finds the max set of compatible activities from a given list of activities
    :param a: list of activities
    :return: lists c and sltn
    """

    # Sort the activities in increasing order of finishing times
    a.sort(key=lambda x: x.finish)

    n = len(a)

    # Create a list to store the max number of compatible activities that end at the ith activity.
    # For example c[3] is the max number of compatible activities in the set a_0, a_1, a_2, a_3.
    c = [1 for i in range(n)]

    # Create a list to store the largest list of compatible activities that end at the ith activity.
    # For example sltn[3] is the largest list of compatible activities in the set a_0, a_1, a_2, a_3.
    # In other words, sltn[3] includes the activities of c[3]
    sltn = [[i] for i in range(n)]

    # Loop through each activity
    for i in range(n):

        # Consider each j less than i
        for j in range(0, i):

            if a[i].is_compatible(a[j]) and c[i] < c[j] + 1:
                # Note that c[j] is the max number of activities from c[0] to c[j]. With the i_th activity c[i]
                # becomes c[j] + 1
                c[i] = c[j] + 1
                sltn[i] = deepcopy(sltn[j])
                sltn[i].append(i)

    return c, sltn


if __name__ == '__main__':
    start_times = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    finish_times = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

    # start_times = [1, 3, 5, 11, 13]
    # finish_times = [4, 8, 12, 14, 14]

    activities = list()

    for i in range(len(start_times)):
        activities.append(Activity(start_times[i], finish_times[i]))

    c, sltn = find_max_set_of_compatible_activities(activities)

    # Print the max number of activities
    for i in c:
        print(i)

    print('')

    # Print the compatible activities
    for i in sltn:
        print(i)



