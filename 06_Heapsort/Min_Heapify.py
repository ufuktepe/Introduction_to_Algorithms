class MinHeap():
    def __init__(self, lst):
        self.lst = lst
        self.idx_dict = {}
        self.build_min_heap()

    def build_idx_dict(self):
        """
        Resets and updates the self.idx_dict
        :return: None
        """
        self.idx_dict = {}
        for i in range(len(self.lst)):
            self.idx_dict[self.lst[i]] = i

    def min_heapify(self, i):
        """
        Assumes the left and right child binary trees of self.lst[i] are min-heaps.
        Floats down the value at self.lst[i] to its correct position so that the subtree rooted at index i obeys the min heap
        property.
        Time complexity: O(log n)
        :param i: index of the item to be positioned
        :return: None
        """

        left = 2 * i + 1
        right = 2 * i + 2

        heap_size = len(self.lst)

        # Check if the left node is smaller than the current node
        if heap_size > left and self.lst[left] < self.lst[i]:
            min_idx = left
        else:
            min_idx = i

        # Check if the right node is smaller than the self.lst[min_idx]
        if heap_size > right and self.lst[right] < self.lst[min_idx]:
            min_idx = right

        # If self.lst[i] is not the min, swap self.lst[min_idx] with self.lst[i] and call min_heapify again
        if min_idx != i:
            self.lst[i], self.lst[min_idx] = self.lst[min_idx], self.lst[i]
            self.min_heapify(min_idx)

    def build_min_heap(self):
        """
        Builds a min-heap and the idx_dict.
        Time complexity: O(n)
        :param self.lst: input array
        :return: None
        """
        for i in range(len(self.lst) // 2, -1, -1):
            self.min_heapify(i)

        self.build_idx_dict()

    def extract_min(self):
        """
        Removes and returns the item with the minimum key (self.lst[0]).
        :return: item with the smallest key
        """

        if len(self.lst) < 1:
            raise IndexError()

        min = self.lst[0]

        # Replace the first item with the last item
        self.lst[0] = self.lst[-1]

        # Remove the last item
        del self.lst[-1]

        # Restore the min heap property
        self.build_min_heap()

        return min

    def restore_min_heap_property(self, i):
        """
        Finds the correct position for self.lst[i] by traversing the tree from i to the root.
        Recursively compares the value of the child node to its parent and swaps the child and parent if child has smaller
        value.
        Finally, builds the idx_dict.
        :param i: index of the child node
        :return: none
        """

        if i == 0:
            return

        parent_idx = (i - 1) // 2

        if self.lst[parent_idx] > self.lst[i]:
            # Swap the parent with the child
            self.lst[i], self.lst[parent_idx] = self.lst[parent_idx], self.lst[i]
            # Check if the position of self.lst[parent_idx] is correct
            self.restore_min_heap_property(parent_idx)

        self.build_idx_dict()

    def min_heap_insert(self, node):
        """
        Inserts a node to a min heap.
        :param node: node to be inserted in the min heap
        :return: None
        """
        self.lst.append(node)
        self.restore_min_heap_property(len(self.lst) - 1)

    def heap_decrease_key(self, i, key):
        """
        Sets the value of self.lst[i] to key and calls restore_min_heap_property to find the correct position for the value of
        self.lst[i].
        :param i: index of the item whose value will be updated
        :param key: new value for self.lst[i]
        :return: None
        """

        # Check if the new value is larger than the current value
        if key > self.lst[i].key:
            print('new key is larger than current key.')
            return

        # Update the value of self.lst[i] to its new value
        self.lst[i].key = key

        # Restore the min-heap property
        self.restore_min_heap_property(i)
