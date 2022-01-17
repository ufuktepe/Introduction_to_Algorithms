from random import randint


class Quicksort:

    @staticmethod
    def partition(lst, p, r):
        """
        Chooses a random item as pivot, places this pivot item at its correct position in the sorted array,
        places all items to the left of the pivot which are less than or equal to the pivot,
        places all items to the right of the pivot which are greater than the pivot

        @param lst: input list to be sorted
        @param p: starting index
        @param r: ending index
        @return: index of the pivot item
        """

        # largest index that has value less than or equal to lst[r]. initialize it to p - 1.
        i = p - 1

        # Randomize: select a randomly chosen item in the array and swap lst[r] with that item
        random_idx = randint(p, r)
        lst[r], lst[random_idx] = lst[random_idx], lst[r]

        # Iterate from p to r - 1
        for j in range(p, r):
            if lst[j] <= lst[r]:
                # Increment i to get the smallest index that has value greater than lst[r]
                i += 1

                # Swap lst[i] and lst[j]
                lst[i], lst[j] = lst[j], lst[i]

                # Now i is the largest index that has value less than or equal to lst[r]

        # Swap lst[i + 1] and lst[r] so that lst[i + 1] is strictly less than all values in lst[i + 2, ..., r]
        lst[i + 1], lst[r] = lst[r], lst[i + 1]

        return i + 1

    @staticmethod
    def quicksort(lst, p, r):
        if p < r:
            q = Quicksort.partition(lst, p, r)
            print(f'{p}, {q}, {r}')
            Quicksort.quicksort(lst, p, q - 1)
            Quicksort.quicksort(lst, q + 1, r)


# sample = [1, 8, 7, 2, 3, 5, 6, 4]
# Quicksort.quicksort(sample, 0, len(sample) - 1)
#
# print(sample)