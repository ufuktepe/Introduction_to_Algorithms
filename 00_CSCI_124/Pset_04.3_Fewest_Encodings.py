

def find_encoding_length_1_based(D, S):
    n = len(S)
    m = len(D)
    E = [float('inf') for x in range(n + 1)]  # 1-based
    ES = [None for x in range(n + 1)]

    E[0] = 0

    # Loop 1 thru n
    for i in range(1, n+1):
        # Loop 1 thru m
        for j in range(1, m+1):

            k = i - len(D[j-1])
            if k >= 0 and S[k:i] == D[j-1]:
                print(f'D[{j-1}]={D[j-1]}')
                if E[i] > E[k] + 1:
                    E[i] = E[k] + 1
                    print(f'E[{i}]={E[i]}')
                    ES[i] = D[j-1]
    return E, ES


def find_encoding_length(D, S):
    n = len(S)
    m = len(D)
    E = [float('inf') for x in range(n + 1)]  # 1-based
    ES = [None for x in range(n + 1)]

    E[0] = 0

    for i in range(n):
        for j in range(m):
            k = i - len(D[j]) + 1
            if k >= 0 and S[k:i + 1] == D[j]:
                print(f'D[{j}]={D[j]}')
                if E[i + 1] > E[k] + 1:
                    E[i + 1] = E[k] + 1
                    print(f'L[{i + 1}]={E[i + 1]}')
                    ES[i + 1] = D[j]
    return E, ES


def print_encoding(ES, j):
    last_encoding = ES[j]
    k = j - len(last_encoding)

    if k > 0:
        print_encoding(ES, k)

    print(last_encoding, end=',')


if __name__ == '__main__':
    S = 'bababbaababa'
    D = ['a', 'ba', 'abab', 'b']
    L, ES = find_encoding_length_1_based(D, S)
    print(L[-1])

    print_encoding(ES, len(S))