def matrix_chain_order(dim):
    """
    Finds the min cost (number of scalar multiplications) for multiplying a chain of matrices.
    :param dim: Sequence of matrix dimensions where matrix A_i has dimensions dim[i] x dim[i + 1]
    :return: lists for min cost and optimal index, respectively
    """

    # Calculate the total number of matrices
    total_length = len(dim) - 1

    # Min cost dictionary where min_cost[(i, j)] equals the min cost for multiplying a chain of matrices from A_i to A_j
    min_cost = dict()

    # Optimal index dictionary where optimal_index[(i, j)] equals an optimal index k such that i<=k<j and multiplying
    # from A_i to Ak, A_k+1 to A_j, and multiplying those 2 resulting matrices yields the minimum cost
    optimal_index = dict()

    # Set the minimum costs for chains of length 1 to zero
    for i in range(total_length):
        min_cost[(i, i)] = 0

    # Calculate the minimum costs for each chain length starting from chain length = 2
    for chain_length in range(2, total_length + 1):
        for i in range(total_length - chain_length + 1):
            j = i + chain_length - 1
            min_cost[(i, j)] = float('inf')

            # Calculate the min cost for (i, j). That is, the min cost for multiplying from matrix A_i to matrix A_j
            # Loop through i to j-1 to find the optimal index that yields the min cost.
            for k in range(i, j):
                # Calculate the min cost for multiplying from A_i to Ak, A_k+1 to A_j, and multiplying those 2
                # resulting matrices. Note that min_cost[(i, k)] and min_cost[(k + 1, j)] should already be
                # calculated in previous loops.
                cost = min_cost[(i, k)] + min_cost[(k + 1, j)] + dim[i] * dim[k + 1] * dim[j + 1]
                if cost < min_cost[(i, j)]:
                    min_cost[(i, j)] = cost
                    optimal_index[(i, j)] = k

    return min_cost, optimal_index


def print_optimal_indices(optimal_index, i, j):
    if i == j:
        print(i, end=',')
    else:
        k = optimal_index[(i, j)]
        print('(', end='')
        print_optimal_indices(optimal_index, i, k)
        print_optimal_indices(optimal_index, k + 1, j)
        print(')', end='')


if __name__ == '__main__':
    dimension_sequence = [30, 35, 15, 5, 10, 20, 25]
    num_of_matrices = len(dimension_sequence) - 1
    min_cost, optimal_index = matrix_chain_order(dimension_sequence)
    print(min_cost[(0, num_of_matrices - 1)])
    print_optimal_indices(optimal_index, 0, num_of_matrices - 1)