import math


def print_neatly(words, n, M):
    cost = [float('inf') for j in range(0, n + 1)]
    cost[0] = 0

    s = [None for j in range(0, n + 1)]

    extras = [[float('inf') for j in range(0, n + 1)] for i in range(0, n + 1)]

    # Penalty matrix
    p = [[float('inf') for j in range(0, n + 1)] for i in range(0, n + 1)]

    for j in range(1, n + 1):
        k = max(0, j - math.ceil(M / 2))
        for i in range(j, k, -1):
            # print(f'i:{i}, j:{j}')
            # Compute extra[i][j]
            if i == j:
                # This is the same as extra[j][j]
                extras[i][j] = M - len(words[j-1])
            else:
                # print(f'extras[{i+1}][{j}]={extras[i+1][j]}')
                # print(f'len(words[{i-1}])={len(words[i-1])}')
                extras[i][j] = extras[i + 1][j] - len(words[i-1]) - 1

            # print(f'extras[{i}][{j}]={extras[i][j]}')

            if extras[i][j] < 0:
                p[i][j] = float('inf')
            elif j == n and extras[i][j] >= 0:
                p[i][j] = 0
            else:
                p[i][j] = (extras[i][j])**3

            # print(f'lc[{i}][{j}]={lc[i][j]}')
            # print(f'cost[{i-1}]={cost[i-1]}')
            # print(f'cost[{j}]={cost[j]}')

            if cost[i - 1] + p[i][j] < cost[j]:
                cost[j] = cost[i - 1] + p[i][j]
                s[j] = i
                # print(f'cost[{j}]={cost[j]}')

    return cost, s


def display_paragraph(words, s, j):
    i = s[j]

    if i != 1:
        display_paragraph(words, s, i - 1)

    line_str = ''
    for k in range(i, j + 1):
        line_str += words[k - 1] + ' '
    print(line_str[:-1])


if __name__ == '__main__':

    words = ['aaa', 'bbb', 'cc', 'dddd', 'eeee', 'ff', 'gg', 'hhhhh']

    f = open('/Users/burak/Downloads/prob2b.txt', 'r')
    content = f.read()
    words = content.split(' ')

    n = len(words)
    M = 40

    cost, s = print_neatly(words, n, M)
    print(f'COST:{cost[n]}')
    display_paragraph(words, s, n)