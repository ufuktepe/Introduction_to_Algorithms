
class Item():
    def __init__(self, w, v):
        self.weight = w
        self.value = v


def get_max(val_1, val_2):
    if val_1 > val_2:
        return val_1
    return val_2


def knapsack(items, capacity, target_profit):
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
    # Hence, column 0 has value 0 for each row.
    # dp[i][j] represents the maximum value of items using items 1 to i and the capacity of the knapsack is j.
    dp = [[0 if i == 0 or j == 0 else None for j in range(target_profit + 1)] for i in range(n + 1)]

    w = [[0 for j in range(target_profit + 1)] for i in range(n + 1)]

    for i in range(len(dp)):
        dp[i][0] = 1


    # Loop through each row starting with row 1. Note that row 0 has 0 values.
    for i in range(1, n + 1):

        # Loop through each column starting with column 1. Note that column 0 has 0 values.
        for j in range(1, target_profit + 1):

            item_weight = items[i - 1].weight
            item_val = items[i - 1].value

            # Note that current item is items[i - 1] which corresponds to dp[i][j] since i ranges from 1 to n.

            if item_val <= j and item_weight + w[i-1][j-item_val] <= capacity and dp[i-1][j-item_val] == 1:
                dp[i][j] = 1
                if w[i - 1][j] > 0:
                    w[i][j] = min(w[i - 1][j], w[i - 1][j - item_val] + item_weight)
                else:
                    w[i][j] = w[i - 1][j - item_val] + item_weight
            else:
                dp[i][j] = dp[i - 1][j]
                w[i][j] = w[i - 1][j]

            # if item_val > j or item_weight > capacity:
            #     dp[i][j] = dp[i - 1][j]
            #     w[i][j] = w[i - 1][j]
            # else:
            #     remaining_weight = w[i - 1][j - item_val]
            #     new_weight = remaining_weight + item_weight
            #
            #     rem_val = dp[i - 1][j - item_val]
            #
            #     if new_weight <= capacity and rem_val == 1:
            #         if dp[i - 1][j] == 1 and w[i - 1][j] < new_weight:
            #             dp[i][j] = dp[i - 1][j]
            #             w[i][j] = w[i - 1][j]
            #         else:
            #             dp[i][j] = 1
            #             w[i][j] = new_weight
            #     else:
            #         dp[i][j] = dp[i - 1][j]
            #         w[i][j] = w[i - 1][j]

    return dp, w


if __name__ == '__main__':
    weight = [2, 1, 6, 3, 5, 4]
    value = [1, 6, 5, 4, 5, 4]

    items = list()

    for i in range(len(weight)):
        items.append(Item(weight[i], value[i]))

    capacity = 10

    dp, w = knapsack(items, capacity, target_profit=10)

    # print the profit table
    print('\nPROFIT TABLE')
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            print('{:<10}'.format(dp[i][j]), end='')
        print('')

    # print the weight table
    print('\nWEIGHT TABLE')
    for i in range(len(w)):
        for j in range(len(w[i])):
            print('{:<10}'.format(w[i][j]), end='')
        print('')