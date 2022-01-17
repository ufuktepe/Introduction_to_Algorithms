import sys


def optimal_bst(p):
    """
    Finds the optimal binary search tree given a list of probabilities.
    :param p: probability list
    :return: expected cost table and root table
    """
    n = len(p)

    # Initialize the expected cost table.
    # e[i][j] defines the expected cost for a binary tree containing the keys k_i,...,k_j
    # Note that the expected cost for e[x][x] is p[x] since the tree contains a single node k_x that has
    # probability p[x]
    e = [[p[i] if j == i else None for j in range(n)] for i in range(n)]

    # Initialize the probability table (also known as frequency).
    # w[i][j] defines the sum of all the probabilities in a binary tree containing the keys k_i,...,k_j
    # Note that the probability for w[x][x] is p[x] since the tree contains a single node k_x that has
    # probability p[x]
    w = [[p[i] if j == i else None for j in range(n)] for i in range(n)]

    # stores tree roots that will be used later for constructing the binary search tree (Needs to be implemented)
    # root[i][j] defines the root (index of p) of a binary tree containing the keys k_i,...,k_j
    # Note that the root for root[x][x] is x since the tree contains a single node k_x
    root = [[i if i == j else None for j in range(n)] for i in range(n)]

    # Loop through each interval length starting from 2 to n
    # Note that length 1 is already populated in e. Because e[x][x] = p[x] (binary tree that has a single node).
    for interval_length in range(2, n + 1):

        # i is the starting index of the interval length
        for i in range(n - interval_length + 1):

            # j is the last index of the interval length
            j = i + interval_length - 1

            # Set the expected cost of searching an optimal binary search tree containing the keys k_j to infinity
            e[i][j] = sys.maxsize

            # Calculate the sum of probabilities for the subtree with keys k_i,...,k_j
            # Note that we already know the sum of probabilities for the subtree with keys k_i,...,k_(j-1)
            w[i][j] = w[i][j - 1] + p[j]

            # Loop through each possible root from i to j
            for r in range(i, j + 1):
                cost = 0

                # Check if r > i. if r == i then the root is k_i and there is no left tree.
                if r > i:
                    # Add the optimal cost for left subtree
                    cost += e[i][r - 1]

                # Check if r < j. if r == j then the root is k_j and there is no right tree.
                if r < j:
                    # Add the optimal cost for right subtree
                    cost += e[r + 1][j]

                # In the new tree (k_i,...,k_j) the depth of each node in the left subtree (w[i][r - 1]) and the right
                # subtree (w[r + 1][j]) increases by 1. Hence, the expected search cost of the new tree (k_i,...,k_j)
                # increases by the sum of all the probabilities in the left and right subtrees.
                # Adding the probability of the root the cost will increase by
                # w[i][r - 1] + p[r] + w[r + 1][j] = w[i][j]
                cost += w[i][j]

                if cost < e[i][j]:
                    e[i][j] = cost
                    root[i][j] = r
    return e, root


if __name__ == '__main__':
    p = [34, 8, 50]
    e, root = optimal_bst(p)

    print(f'Cost of optimal BST: {e[0][-1]}')


