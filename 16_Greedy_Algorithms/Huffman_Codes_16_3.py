import math
from Min_Heapify import *


class Character:
    def __init__(self, v, f):
        self.value = v
        self.frequency = f

        # left child of the character (used for inner nodes)
        self.left = None

        # right child of the character (used for inner nodes)
        self.right = None

    def __lt__(self, other):
        return isinstance(other, Character) and self.frequency < other.frequency

    def __gt__(self, other):
        return isinstance(other, Character) and self.frequency > other.frequency

    def __str__(self):
        if self.left is None and self.right is None:
            return f'Value:{self.value} Frequency:{self.frequency} Left:N/A Right:N/A'
        elif self.left is None:
            return f'Value:{self.value} Frequency:{self.frequency} Left:N/A Right:{self.right.value}'
        elif self.right is None:
            return f'Value:{self.value} Frequency:{self.frequency} Left:{self.left.value} Right:N/A'
        return f'Value:{self.value} Frequency:{self.frequency} Left:{self.left.value} Right:{self.right.value}'


def huffman(characters):
    """
    Builds a code tree from a list of characters in a bottom-up manner.
    It begins with a set of n leaves (given characters) and performs a sequence of n-1 “merging” operations to create
    the final tree.
    :param characters: input list of characters
    :return: the root of the code tree
    """

    # n is the number of characters
    n = len(characters)

    # Create a min heap (min-priority queue) from the given characters
    pq = characters
    build_min_heap(pq)

    # Loop n - 1 times to find the non-leaf nodes of the tree.
    # We know that there must be n - 1 non-leaf nodes because we are building a full binary tree and there are n
    # leaves (characters) so there must be n - 1 non-leaf nodes
    for i in range(n - 1):

        # Extract the node with the minimum frequency (essentially this is the root node in the min-priority queue).
        # Note that when we perform this action, the extracted node will be removed from the min-priority queue.
        x = extract_min(pq)

        # Extract the next node with the minimum frequency (this is the root node since x is removed from the
        # min-priority queue.
        y = extract_min(pq)

        # Merge nodes x and y. In other words, create a parent node for x and y which has frequency x.frequency +
        # y.frequency
        z = Character('*', x.frequency + y.frequency)
        z.left = x
        z.right = y

        # Insert the parent node in the min-priority queue
        min_heap_insert(pq, z)

    # Return the min-priority queue which should only include the root node
    return pq


if __name__ == '__main__':
    # The following is from Chp 16.3 of CLRS
    char_freq = {'a': 45, 'b': 13, 'c': 12, 'd': 16, 'e': 9, 'f': 5}

    characters = []

    # populate the characters list with Character objects
    for val, freq in char_freq.items():
        characters.append(Character(val, freq))

    pq = huffman(characters)

    # print the tree

    # Populate the nodes list with the root node
    nodes = [pq[0]]

    # Depth of the tree
    depth = 0

    # Number of nodes seen so far
    count = 0

    # Print the nodes by traversing them in a BFS fashion
    while nodes:
        curr_node = nodes[0]
        count += 1

        # Check if the depth needs to be incremented
        if math.trunc(math.log(count, 2)) > depth:
            depth += 1

        print(f'Depth {depth} {curr_node}')

        if curr_node.left is not None:
            nodes.append(curr_node.left)
        if curr_node.right is not None:
            nodes.append(curr_node.right)

        del nodes[0]




