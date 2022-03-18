

def longest_monotone_subsequence(lst):

    I = [1 for x in lst]
    D = [1 for x in lst]

    # These lists are for reconstruction
    I_r = [x for x in lst]
    D_r = [x for x in lst]

    for i in range(len(lst)):
        for j in range(0, i):
            if lst[i] > lst[j]:
                if I[i] < I[j] + 1:
                    I[i] = I[j] + 1
                    I_r[i] = str(I_r[j]) + ',' + str(lst[i])
            elif lst[i] < lst[j]:
                if D[i] < D[j] + 1:
                    D[i] = D[j] + 1
                    D_r[i] = str(D_r[j]) + ',' + str(lst[i])

    incr = 0
    incr_seq = ''
    decr = 0
    decr_seq = ''

    for i in range(len(I)):
        if incr < I[i]:
            incr = I[i]
            incr_seq = I_r[i]

    for i in range(len(D)):
        if decr < D[i]:
            decr = D[i]
            decr_seq = D_r[i]

    print(f'Increasing Sequence: {incr_seq}')
    print(f'Decreasing Sequence: {decr_seq}')


if __name__ == '__main__':
    A = [1, 4, 7, 3, 45, 21, 89, 34, 23, 24, 2]
    longest_monotone_subsequence(A)