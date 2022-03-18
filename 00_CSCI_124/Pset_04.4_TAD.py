import random

def tad(X):
    n = len(X)

    T = [[None for y in range(n)] for x in range(n)]

    S = [float('-inf') for x in range(n + 1)]
    Q = [None for x in range(n)]

    S[0] = 0

    for j in range(n):
        S[j + 1] = S[j]

        for i in range(j, -1, -1):
            if X[i][j] == 0:
                p = -1
            else:
                p = 2

            if j - i > 1:
                T[i][j] = T[i][j-1] + T[i+1][j] - T[i+1][j-1] + p
            elif j != i:
                T[i][j] = T[i][j - 1] + T[i + 1][j] + p
            else:
                T[i][j] = p

            if S[j + 1] < T[i][j] + S[i]:
                S[j + 1] = T[i][j] + S[i]
                Q[j] = i
        print(f'Line {j}: {S[j + 1]}')

    return S[n], Q


def populate_Cij(C, Q, j):

    i = Q[j]

    while(j > 0 and i is None):
        j -= 1
        i = Q[j]

    if i is None:
        return

    for y in range(j, i - 1, -1):
        for x in range(i, y + 1):
            C[x][y] = 1

    if i > 0:
        populate_Cij(C, Q, i - 1)


def print_matrix(X):
    rows = []
    for j in range(len(X)):
        row_str = ''
        for i in range(j+1):
            row_str += str(X[i][j]) + ' '

        rows.append(row_str)

    rows.reverse()
    print('-------------')
    for row in rows:
        print(row)
    print('-------------')



if __name__ == '__main__':
    n = 5
    X = [[0 if random.uniform(0, 1) < 0.7 else 1 for y in range(n)] for x in range(n)]

    print_matrix(X)

    S_n, Q = tad(X)

    print(S_n)

    C = [[0 for y in range(len(Q))] for x in range(len(Q))]

    populate_Cij(C, Q, n-1)

    print_matrix(C)