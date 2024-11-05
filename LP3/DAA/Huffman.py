import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self,data,freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self,other):
        return  self.freq < other.freq
    

def print_codes(root,code,huffman):
    if not root:
        return

    if not root.left and not root.right:
        huffman[root.data] = code
        print(f'{root.data}:{code}')

    print_codes(root.left,code+'0',huffman)
    print_codes(root.right,code+'1',huffman)

def build_tree(text):
    freq = defaultdict(int)
    for ch in text:
        freq[ch]+=1
    
    pq = []
    for data,freqency in freq.items():
        heapq.heappush(pq,HuffmanNode(data,freqency))
    
    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)

        new_node = HuffmanNode('\0',left.freq + right.freq)
        new_node.left = left
        new_node.right = right

        heapq.heappush(pq,new_node)

    root = pq[0]

    huffman_code = {}
    print_codes(root,"",huffman_code)

    print("\nEncoded string :",end="")
    for ch in text:
        print(huffman_code[ch],end="")
    print()

text = input("Enter text to encode : ")
build_tree(text)

