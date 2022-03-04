
def select(arr, k):
    """
    Select a pivot corresponding to the kth largest element in the array
    :param arr: Input array
    :param k: cardinality that represents the kth largest element in the array
    :return: The value of the kth largest elm
    """

    # Divide array into chunks of 5
    # chunks by taking i from 0 to 4, 5 to 9, 10 to 14, etc
    chunks = [arr[i : i+5] for i in range(0, len(arr), 5)]

    # sort each chunk
    sorted_chunks = [sorted(chunk) for chunk in chunks]

    # take the median of each chunk
    medians = [chunk[len(chunk) // 2] for chunk in sorted_chunks]

    # find the median of medians
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2 - 1]
    else:
        pivot = select(medians, len(medians) // 2 - 1)

    # get the index of the pivot and create low and high arrays
    p, arr_low, arr_high = partition(arr, pivot)

    if k - 1 == len(arr_low):
        #select that pivot
        return pivot

    elif k - 1 < len(arr_low):
        #select a new pivot by looking on the left side of the partioning
        return select(arr_low, k)
    else:
        #select a new pivot by looking on the right side of the partioning
        return select(arr_high, k - (len(arr) - len(arr_high)))

def partition(arr, pivot):
    idx = 0
    arr_low = []
    arr_high = []
    found_pivot = False
    for i in range(len(arr)):
        if pivot > arr[i]:
            idx += 1
            arr_low.append(arr[i])
        elif pivot < arr[i]:
            arr_high.append(arr[i])
        elif found_pivot:
            arr_low.append(arr[i])
        else:
            found_pivot = True

    return idx, arr_low, arr_high


if __name__ == '__main__':
    arr = [1, 4, 3, 2, 5, 7, 7, 7, 8, 9, 10]
    k_th_elm = select(arr, 4)
    print(k_th_elm)