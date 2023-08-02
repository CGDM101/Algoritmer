class binaryTree:
    def __init__(self, nodeData, left=None, right=None):
        self.nodeData = nodeData
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.nodeData)


tree = binaryTree("Root")
# Bygger top down här (går att bygga bottom up också)
BranchA = binaryTree("Branch A")
BranchB = binaryTree("Branch B")
tree.left = BranchA
tree.right = BranchB

LeafC = binaryTree("Leaf C")
LeafD = binaryTree("Leaf D")
LeafE = binaryTree("Leaf E")
LeafF = binaryTree("Leaf F")
BranchA.left = LeafC
BranchA.right = LeafD
BranchB.left = LeafE
BranchB.right = LeafF

# Traversera trädet för att se om det fungerar, dvs är balanserat


def traverse(tree):  # obs inorder traversal!
    if tree.left != None:
        traverse(tree.left)  # rekursion
    if tree.right != None:
        traverse(tree.right)  # rekursion
    print(tree.nodeData)


traverse(tree)  # NB! Skriver inget förrän den kommer  till den första lövnoden
# Leaf C
# Leaf D
# Branch A
# Leaf E
# Leaf F
# Branch B
# Root

# Skriver ut vänstras barn först, sedan vänstra, sedan högras barn, sedan högra, sedan roten
