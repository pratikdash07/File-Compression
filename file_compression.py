import heapq
from collections import defaultdict, Counter

# Step 1: Read the file
def read_file(file_path):
    with open(file_path, 'rb') as f:
        return f.read()

# Step 2: Build frequency table and Huffman tree
import heapq
import os
from collections import Counter

class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    frequency = Counter(data)
    heap = [Node(symbol, freq) for symbol, freq in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]

def generate_codes(node, prefix="", codebook={}):
    if node.symbol is not None:
        codebook[node.symbol] = prefix
    else:
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

def save_codebook(codebook, output_path):
    with open(output_path, 'w') as f:
        for byte, code in codebook.items():
            f.write(f"{byte} : {code}\n")

def compress_data(data, codebook):
    return ''.join(codebook[byte] for byte in data)

def write_compressed(output_path, compressed_data):
    compressed_bits = int(compressed_data, 2)
    compressed_size = (compressed_bits.bit_length() + 7) // 8
    with open(output_path, 'wb') as f:
        f.write(compressed_bits.to_bytes(compressed_size, 'big'))
    return compressed_size

# Example usage with codebook output
input_path = "input1.txt"
output_path = "output1.huf"
codebook_path = "codebook1.txt"

# Read and compress the file
file_data = read_file(input_path)
root = build_huffman_tree(file_data)
codebook = generate_codes(root)

# Save codebook for readability
save_codebook(codebook, codebook_path)

compressed_data = compress_data(file_data, codebook)
write_compressed(output_path, compressed_data)
