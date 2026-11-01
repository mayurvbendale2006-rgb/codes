
# Huffman Encoding using Greedy Strategy

import heapq

# Node class
class Node:
    def __init__(self, char=None, left=None, right=None):
        self.char = char
        self.left = left
        self.right = right


# Function to generate Huffman Codes
def huffman_encoding(characters, frequencies):

    heap = []
    count = 0

    # Insert characters into min-heap
    for char, freq in zip(characters, frequencies):
        node = Node(char=char)
        heapq.heappush(heap, (freq, count, node))
        count += 1

    # Build Huffman Tree
    while len(heap) > 1:

        left_freq, _, left = heapq.heappop(heap)
        right_freq, _, right = heapq.heappop(heap)

        new_node = Node(left=left, right=right)

        heapq.heappush(
            heap,
            (left_freq + right_freq, count, new_node)
        )
        count += 1

    # Generate Huffman Codes
    codes = {}

    def generate_codes(node, code):

        if node.char is not None:
            codes[node.char] = code if code else "0"
            return

        generate_codes(node.left, code + "0")
        generate_codes(node.right, code + "1")

    generate_codes(heap[0][2], "")

    return codes


# Main Program
characters = input("Enter characters separated by space: ").split()
frequencies = list(map(int, input("Enter frequencies: ").split()))

if (len(characters) == 0 or
    len(characters) != len(frequencies) or
    len(set(characters)) != len(characters) or
    any(freq <= 0 for freq in frequencies)):

    print("Invalid input")

else:
    codes = huffman_encoding(characters, frequencies)

    print("\nHuffman Codes:")
    print("Character\tCode")

    for char in sorted(codes):
        print(char, "\t\t", codes[char])
