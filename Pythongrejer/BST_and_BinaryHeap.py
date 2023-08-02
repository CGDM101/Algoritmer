# BINARY SEARCH TREE
# Sökning O(log n) tid, jämfört med O(n) för en binary heap. Dock; bygga en binary heap kräver O(n) tid, medan BST kräver O(n log n) tid! Så BST är bättre för sökning än medan binär heap är bättre för byggande...?
import heapq
from bintrees import BinaryTree
print('BINARY SEARCH TREE')

# Key and value pairs, dvs dictionary/hash table

data = {3: 'White', 2: 'Red', 1: 'Green', 5: 'Orange',
        4: 'Yellow', 7: 'Purple', 0: 'Magenta'}

tree = BinaryTree(data)
tree.update({6: 'Teal'})


def displayKeyValue(key, value):
    print('Key: ', key, 'Value: ', value)


tree.foreach(displayKeyValue)
print('Item 3 contains: ', tree.get(3))
print('The maximum item is: ', tree.max_item())

# BINARY HEAP
print('BINARY HEAP')

data = {3: 'White', 2: 'Red', 1: 'Green', 5: 'Orange',
        4: 'Yellow', 7: 'Purple', 0: 'Magenta'}

heap = []
for key, value in data.items():
    heapq.heappush(heap, (key, value))
heapq.heappush(heap, (6, 'Teal'))
heap.sort()

for item in heap:
    print('Key: ', item[0], 'Value: ', item[1])
print('Item 3 contains: ', heap[3][1])
print('The maximum item is: ', heapq.nlargest(1, heap))
