import math


def stooge_sort(lst, i, j):

    # Swap the first and last elements if the first element is larger than the last element
    if lst[i] > lst[j]:
        lst[i], lst[j] = lst[j], lst[i]

    # Find the length for the current array
    array_len = j - i + 1

    # Return if the number of elements is less than or equal to 2
    if array_len <= 2:
        return

    # Find 1/3rd length of the current array
    k = math.floor(array_len * 1 / 3)

    # Sort the first 2/3rd part
    stooge_sort(lst, i, j - k)

    # Sort the last 2/3rd part
    stooge_sort(lst, i + k, j)

    # Sort the first 2/3rd again
    stooge_sort(lst, i, j - k)


if __name__ == '__main__':
    lst = [10, 6, 20]

    stooge_sort(lst, 0, len(lst) - 1)

    print(lst)



