

def universal_sink(a):
    i = 0
    j = 0

    while i < len(a) and j < len(a):
        if i == j or (a[i][j] == 0 and a[j][i] == 1):
            j += 1
        else:
            i += 1
            j = 0

    if j == len(a):
        return True
    return False


if __name__ == '__main__':

    a = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0]
    ]

    print(universal_sink(a))
