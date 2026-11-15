
import heapq
from itertools import count

n = int(input("Enter number of characters: "))
heap = []
unique = count()

for i in range(n):
    ch = input("Enter character: ")
    freq = int(input("Enter frequency: "))
    heapq.heappush(heap, (freq, next(unique), ch))

while len(heap) > 1:
    f1, _, l = heapq.heappop(heap)
    f2, _, r = heapq.heappop(heap)
    heapq.heappush(heap, (f1+f2, next(unique), (l, r)))

huff = {}

def generate(node, code=""):
    if isinstance(node, str):
        huff[node] = code or "0"
    else:
        generate(node[0], code+"0")
        generate(node[1], code+"1")

if heap:
    generate(heap[0][2])

print("\nHuffman Codes:")
for ch, code in huff.items():
    print(ch, ":", code)

msg = input("\nEnter message to encode: ")
encoded = "".join(huff[ch] for ch in msg)
print("Encoded message:", encoded)
