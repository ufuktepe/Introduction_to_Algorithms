
class Item():
    def __init__(self, w, v):
        self.weight = w
        self.value = v


def get_max(val_1, val_2):
    if val_1 > val_2:
        return val_1
    return val_2


def knapsack(items, c):
    """
    Finds the maximum total value of items that can be put in a knapsack which has capacity c.
    :param items: list of items
    :param c:
    :return:
    """

    # n is the number of items
    n = len(items)

    # Create the dynamic programming table and populate the first column and first row with zeros.
    # The rows represent the item numbers. Note that row 0 represents an empty set hence it has zero values for any j.
    # The columns represent the capacity of the knapsack. Note that column 0 represents a knapsack with 0 capacity.
    # Hence column 0 has 0 values for each row.
    # dp[i][j] represents the maximum value of items using items 1 to i and the capacity of the knapsack is j.
    dp = [[0 if i == 0 or j == 0 else None for j in range(c + 1)] for i in range(n + 1)]

    # Loop through each row starting with row 1. Note that row 0 has 0 values.
    for i in range(1, n + 1):

        # Loop through each column starting with column 1. Note that column 0 has 0 values.
        for j in range(1, c + 1):

            # Note that current item is items[i - 1] which corresponds to dp[i][j] since i ranges from 1 to n.

            # The value of dp[i][j] is either one of the following 2 options:
            # 1. Exclude the current item, take the value of the subarray with the same capacity -> dp[i - 1][j]
            # 2. Include the current item if its weight is not more than the capacity. In this case include the
            # current item's value plus whatever value we get from the remaining capacity and remaining items
            # dp[i][j] = max( dp[i - 1][j], items[i - 1].value + dp[i - 1][j - items[i - 1].weight] )
            if items[i - 1].weight <= j:
                remaining_weight = j - items[i - 1].weight
                value_1 = items[i - 1].value + dp[i - 1][remaining_weight]
                value_2 = dp[i - 1][j]

                dp[i][j] = get_max(value_1, value_2)

            else:
                dp[i][j] = dp[i - 1][j]

    return dp


if __name__ == '__main__':
    weight = [1, 2, 3, 5]
    value = [1, 6, 10, 16]

    items = list()

    for i in range(len(weight)):
        items.append(Item(weight[i], value[i]))

    capacity = 7

    dp = knapsack(items, capacity)

    # print the table
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            print('{:<10}'.format(dp[i][j]), end='')
        print('')