def lcs_length(x, y):
    """
    Finds the longest common subsequence (LCS) of two substrings.
    :param x: first string
    :param y: second string
    :return: lcs_len and lcs lists.
    lcs_len defines the length of an LCS. For example, lcs_len[2, 4] is the length of an LCS of the sequence x_2
    and y_4. Note that x_0 and y_0 are zero length (empty) sequences.
    lcs includes the longest common subsequence for each pairs of sequence. For example, lcs[7, 6] is the LCS of x_7
    and y_6.
    """
    m = len(x)
    n = len(y)

    # Initialize the output list with zeros. Essentially this is a table where elements of x form the rows and
    # elements of y form the columns. i.e. lcs_len[6, 3] defines the length of an LCS of the sequence x_6 and y_3.
    lcs_len = [[0 for a in range(n + 1)] for b in range(m + 1)]

    # Initialize the list for longest common subsequences.
    lcs = [['' for a in range(n + 1)] for b in range(m + 1)]

    # The for loop below builds lcs_len[m + 1][n + 1] in a bottom-up fashion.
    # lcs_len contains length of LCS for already computed sub-problems

    # Loop through each row
    for i in range(1, m + 1):

        # loop through each column
        for j in range(1, n + 1):

            # If the current characters of x and y match then the length of LCS is lcs_len[i - 1][j - 1] + 1
            if x[i - 1] == y[j - 1]:
                lcs_len[i][j] = lcs_len[i - 1][j - 1] + 1
                lcs[i][j] += lcs[i - 1][j - 1] + x[i - 1]

            # If the current characters of x and y do not match then LCS is max(lcs_len[i - 1][j], lcs_len[i][j - 1])
            elif lcs_len[i - 1][j] >= lcs_len[i][j - 1]:
                lcs_len[i][j] = lcs_len[i - 1][j]
                lcs[i][j] = lcs[i - 1][j]
            else:
                lcs_len[i][j] = lcs_len[i][j - 1]
                lcs[i][j] = lcs[i][j - 1]

    return lcs_len, lcs


if __name__ == '__main__':
    x = 'ABCBDAB'
    y = 'BDCABA'

    lcs_len_list, lcs_list = lcs_length(x, y)

    # Print the lcs_len table
    for i in range(len(x) + 1):
        for j in range(len(y) + 1):
            print(lcs_len_list[i][j], end='  ')
        print('')

    print(f'Length of LCs is {lcs_len_list[len(x)][len(y)]}\n')

    # Print the lcs table
    for i in range(len(x) + 1):
        for j in range(len(y) + 1):
            # Print chars of y in the first row
            if i == 0 and j != 0:
                print("{:<10}".format(y[j - 1]), end='')
            # Print chars of x in the first column
            elif i != 0 and j == 0:
                print("{:<10}".format(x[i - 1]), end='')
            # Print the LCS
            else:
                print("{:<10}".format(lcs_list[i][j]), end='')
        print('')




