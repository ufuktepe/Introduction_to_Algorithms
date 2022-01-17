def cut_rod(prices, n, level):
    """
    Naively finds the best way to cut a rod of length n where the rod of length `i` has a revenue `prices[i-1]`
    :param prices: array of prices (index + 1 = length)
    :param n: length of the rod
    :param level: leading whitespace representing the recursion level (each recursion level has 3 whitespaces)
    :return: maximum revenue possible
    """

    # Base case
    if n == 0:
        return 0

    max_revenue = float('-inf')

    # one by one, partition the given rod of length `n` into two parts of length
    # (1, n-1), (2, n-2), (3, n-3), … ,(n-1, 1), (n, 0) and take the maximum
    for i in range(1, n + 1):
        print(f'{level}Evaluating P_{i} + R_{n - i}')

        # Calculate the max revenue for length n - i
        level += '   '
        r = cut_rod(prices, n - i, level)
        level = level[:-3]

        # rod of length `i` has a revenue `prices[i-1]`
        current_revenue = prices[i - 1] + r

        if max_revenue < current_revenue:
            max_revenue = current_revenue
        print(f'{level}P_{i}:{prices[i - 1]} + R_{n - i}:{r} = {current_revenue} Max Revenue:{max_revenue}')

    return max_revenue


def memoized_cut_rod(prices, n):
    """
    Initializes the revenues list with negative infinity and calls memoized_cut_rod_aux.
    :param prices: array of prices (index + 1 = length)
    :param n: length of the rod
    :return: maximum revenue possible
    """
    revenues = [float('-inf') for i in range(n)]
    return memoized_cut_rod_aux(prices, n, revenues, '')


def memoized_cut_rod_aux(prices, n, revenues, level):
    """
    Finds the best way to cut a rod of length n where the rod of length `i` has a revenue `prices[i-1]`
    Uses a top-down approach
    :param prices: array of prices (index + 1 = length)
    :param n: length of the rod
    :param revenues: array of max revenues (index + 1 = length)
    :param level: leading whitespace representing the recursion level (each recursion level has 3 whitespaces)
    :return: maximum revenue possible
    """

    # Base case
    if n == 0:
        return 0

    # Return the max revenue if it has already been calculated before
    if revenues[n - 1] != float('-inf'):
        return revenues[n - 1]

    max_revenue = float('-inf')

    # one by one, partition the given rod of length `n` into two parts of length
    # (1, n-1), (2, n-2), (3, n-3), … ,(n-1, 1), (n, 0) and take the maximum
    for i in range(1, n + 1):
        print(f'{level}Evaluating P_{i} + R_{n - i}')

        # Calculate the max revenue for length n - i
        level += '   '
        r = memoized_cut_rod_aux(prices, n - i, revenues, level)
        level = level[:-3]

        # rod of length `i` has a revenue `prices[i-1]`
        current_revenue = prices[i - 1] + r

        if current_revenue > max_revenue:
            max_revenue = current_revenue
        print(f'{level}P_{i}:{prices[i - 1]} + R_{n - i}:{r} = {current_revenue} Max Revenue:{max_revenue}')

    # Save the max revenue for length n in the revenues list
    revenues[n - 1] = max_revenue

    return max_revenue


def bottom_up_cut_rod(prices, n):
    """
    Finds the best way to cut a rod of length n where the rod of length `i` has a revenue `prices[i-1]`
    Uses a bottom-up approach (no recursion)
    :param prices: array of prices (index + 1 = length)
    :param n: length of the rod
    :return: maximum revenue possible
    """

    # Create a revenues list. The index identifies the length of the rod (index = length)
    revenues = [float('-inf') for x in range(n + 1)]
    # Set the revenue for length 0 to 0
    revenues[0] = 0

    # Start with a rod of length 1 and increase the length one by one up to length n
    for j in range(1, n + 1):
        max_revenue = float('-inf')
        # i represents the length of the first piece. Increase the length of the first piece starting from 1 to j
        for i in range(1, j + 1):
            # Find the revenue for length i + length (j - i)
            current_revenue = prices[i - 1] + revenues[j - i]
            print(f'P_{i} + R_{j - i} = {current_revenue}')
            if current_revenue > max_revenue:
                max_revenue = current_revenue

        revenues[j] = max_revenue
        print(f'revenues[{j}]:{max_revenue}')

    return revenues[n]


def extended_bottom_up_cut_rod(prices, n):
    """
    Finds the best way to cut a rod of length n where the rod of length `i` has a revenue `prices[i-1]`
    Uses a bottom-up approach (no recursion)
    :param prices: array of prices (index + 1 = length)
    :param n: length of the rod
    :return: list of revenues and optimal first piece sizes
    """

    # Create a revenues list. The index identifies the length of the rod (index = length)
    revenues = [float('-inf') for x in range(n + 1)]
    # Set the revenue for length 0 to 0
    revenues[0] = 0

    # Create a list for the optimal size of the first piece. The index identifies the length of the rod (index = length)
    first_piece_sizes = [float('-inf') for x in range(n + 1)]
    first_piece_sizes[0] = 0

    # Start with a rod of length 1 and increase the length one by one up to length n
    for j in range(1, n + 1):
        max_revenue = float('-inf')
        # i represents the length of the first piece. Increase the length of the first piece starting from 1 to j
        for i in range(1, j + 1):
            # Find the revenue for length i + length (j - i)
            current_revenue = prices[i - 1] + revenues[j - i]

            if current_revenue > max_revenue:
                max_revenue = current_revenue
                first_piece_sizes[j] = i

        revenues[j] = max_revenue
        print(f'revenues[{j}]:{max_revenue}')

    return revenues, first_piece_sizes


if __name__ == '__main__':
    prices = [1, 5, 8, 9]
    prices_long = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    # # Example for the naive solution
    # print(cut_rod(prices, len(prices), ''))

    # # Example for the top-down method with memoization
    # print(memoized_cut_rod(prices, len(prices)))

    # # Example for the bottom-up method with memoization
    # print(bottom_up_cut_rod(prices, len(prices)))

    # Example for the extended bottom-up method with memoization
    revenues, first_piece_sizes = extended_bottom_up_cut_rod(prices_long, len(prices_long))
    print(revenues)
    print(first_piece_sizes)





