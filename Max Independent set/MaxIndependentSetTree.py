import sys
sys.stdout.reconfigure(encoding='utf-8')
from anytree import Node, RenderTree

# Create tree
root = Node("root")
B = Node("B", parent=root)
C = Node("C", parent=root)
D = Node("D", parent=root)
E = Node("E", parent=B)
F = Node("F", parent=B)
G = Node("G", parent=C)
H = Node("H", parent=C)
I = Node("I", parent=D)
J = Node("J", parent=D)
K = Node("K", parent=G)
L = Node("L", parent=K)
M = Node("M", parent=K)
N = Node("N", parent=M)
O = Node("O", parent=M)

# Display the tree
print("Original Tree:")
for pre, fill, node in RenderTree(root):
    print(f"{pre}{node.name}")

# Calculate Max Independent Set
def maxIndependentSetTree(Root):
    IndependentSet = []
    unCutNodesSet = {Root} | set(Root.descendants)

    def IndependentSetIteration (Root):
        if Root.is_leaf == True:
            IndependentSet.append(Root)
            if Root.parent is not None:
                Root.parent.parent = None
            if Root.parent in unCutNodesSet:
                unCutNodesSet.remove(Root.parent)
            Root.parent = None
            unCutNodesSet.remove(Root)
        else :
            for child in Root.children:
                IndependentSetIteration(child)

    while unCutNodesSet:
        IndependentSetIteration (next(iter(unCutNodesSet)))
    return IndependentSet

print(maxIndependentSetTree(root))