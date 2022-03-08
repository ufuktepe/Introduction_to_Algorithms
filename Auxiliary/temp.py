

def sort_in_place(A, B):
    i = 0
    j = len(A) - 1

    for k in range(len(A)):
        if A[i] in B:
            i += 1
        else:
            A[i], A[j] = A[j], A[i]
            j -= 1

    return A


def dynamic_programming(n):

    for d in range(1, n):
        for i in range(1, n-d+1):
            j = i + d
            print(f"indict(s[{i}, {j}])")
            print('else')
            for k in range(i+1, j):
                print(f'if D({i},{k}) and D({k},{j}) then D({i},{j})  ')


if __name__ == '__main__':
    # A = [3, 5, 7, 2, 6, 4]
    # B = {72, 2, 7}
    #
    # sort_in_place(A, B)
    # print(A)

    dynamic_programming(4)