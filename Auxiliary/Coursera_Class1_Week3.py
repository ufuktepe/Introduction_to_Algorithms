import math


def partition(lst, low, high):

    # Swap first and last elms
    lst[low], lst[high] = lst[high], lst[low]

    # # Find the lowest of the first, median, and last items
    # lst_len = (high - low + 1)
    # if lst_len % 2 == 1:
    #     mid = math.floor(lst_len / 2) + low
    # else:
    #     mid = int(lst_len / 2 - 1) + low
    #
    # if (lst[low] < lst[mid] < lst[high]) or (lst[low] > lst[mid] > lst[high]):
    #     lst[low], lst[mid] = lst[mid], lst[low]
    # elif (lst[low] < lst[high] < lst[mid]) or (lst[low] > lst[high] > lst[mid]):
    #     lst[low], lst[high] = lst[high], lst[low]

    pivot = lst[low]
    # print(f'median: {pivot}')
    i = low + 1

    for j in range(low + 1, high + 1):
        if lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1

    lst[i - 1], lst[low] = lst[low], lst[i - 1]

    return i - 1


def quicksort(lst, low, high, count):

    if low < high:
        count += (high - low)
        # print(str(high - low))
        q = partition(lst, low, high)
        count = quicksort(lst, low, q - 1, count)
        count = quicksort(lst, q + 1, high, count)

    return count


txt_file = open("/Users/burak/Downloads/sample.txt", 'r')

sample = list()

for line in txt_file:
    sample.append(int(line.strip()))

print("done with the list")

# sample = [2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]

count = quicksort(sample, 0, len(sample) - 1, 0)

print(sample)
print(count)
