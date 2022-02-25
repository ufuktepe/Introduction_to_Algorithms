

def rank(lst, x):
    count = 0
    for item in lst:
        if item <= x:
            count += 1
    return count


def median(lst):
    lst.sort()
    mid = len(lst) // 2

    return lst[mid]


def select(lst, k):
    lst_a = []
    lst_b = []
    n = len(lst)
    for i in range(n//5):
        group = [lst[5*i], lst[5*i + 1], lst[5*i + 2], lst[5*i + 3], lst[5*i + 4]]
        m = median(group)
        lst_a.append(m)

    x = select(lst_a, n//10)

    if rank(x) > k:
        for j in lst:
            if j <= x:
                lst_b.append(j)
        return select(lst_b, k)
    else:
        for j in lst:
            if j >= x:
                lst_b.append(j)
        return select(lst_b, k + len(lst_b) - len(lst))


if __name__ == '__main__':
    lst = [3, 5, 1, 7, 9, 8, 6, 4, 2, 0]

    print(select(lst, 3))