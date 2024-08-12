import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_codes(root, current_code, codes):
    if root is None:
        return
    
    if root.char is not None:
        codes[root.char] = current_code
        return
    
    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)

def huffman_encoding(data):
    if not data:
        return "", None
    
    frequencies = Counter(data)
    root = build_huffman_tree(frequencies)
    codes = {}
    generate_codes(root, "", codes)
    
    encoded_data = "".join(codes[char] for char in data)
    return encoded_data, root

def huffman_decoding(encoded_data, root):
    decoded_output = []
    current_node = root
    
    for bit in encoded_data:
        current_node = current_node.left if bit == '0' else current_node.right
        
        if current_node.char is not None:
            decoded_output.append(current_node.char)
            current_node = root
    
    return "".join(decoded_output)

def menu():
    while True:
        print("\nHuffman Encoding Program")
        print("1. Encode a String")
        print("2. Decode a String")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            data = input("Enter the string to encode: ")
            encoded_data, tree = huffman_encoding(data)
            if tree:
                print(f"Encoded string: {encoded_data}")
            else:
                print("Unable to encode an empty string.")
        
        elif choice == '2':
            encoded_data = input("Enter the Huffman encoded string: ")
            if 'tree' in locals():
                decoded_data = huffman_decoding(encoded_data, tree)
                print(f"Decoded string: {decoded_data}")
            else:
                print("Please encode a string first to generate the Huffman tree.")
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    menu()
