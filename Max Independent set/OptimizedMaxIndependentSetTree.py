class Node:
    # Conplexity O(n)
    def __init__(self, data, parent, tree):
        self.data = data
        self.parent = parent
        self.children = set()
        self.tree = tree
        if tree == None:
            raise "Error : Node have not tree"
        if parent != None:
            parent.children.add(self)
            if parent in tree.leafs:
                tree.leafs.remove(self.parent)
        tree.leafs.add(self)

    #Complexity O(1)
    def remove_leaf(self):
        if self.is_leaf() == False:
            return
        self.tree.leafs.remove(self)
        par = self.parent
        self.parent = None
        if par and par.is_leaf():
            self.tree.leafs.add(par)

    # Complexity O(n)
    def degree(self):
        num = 0
        for child in self.children:
            num += child.degree()
        num += 1
        return num

    # Complexity O(1)
    def is_leaf(self):
        return not self.children

class Tree:
    # Complexity this O(1) Overall O(n)
    def __init__(self, root):
        self.root = root
        self.leafs = set() # access to the tree leaf at O(1)

    # Complexity this O(1) Overall O(n)
    def degree(self):
        return self.root.degree()

tree = Tree(None)
root = Node("root", None, tree)
tree.root = root

B = Node("B", parent=root, tree=tree)
C = Node("C", parent=root, tree=tree)
D = Node("D", parent=root, tree=tree)
E = Node("E", parent=B, tree=tree)
F = Node("F", parent=B, tree=tree)
G = Node("G", parent=C, tree=tree)
H = Node("H", parent=C, tree=tree)
I = Node("I", parent=D, tree=tree)
J = Node("J", parent=D, tree=tree)
K = Node("K", parent=G, tree=tree)
L = Node("L", parent=K, tree=tree)
M = Node("M", parent=K, tree=tree)
N = Node("N", parent=M, tree=tree)
O = Node("O", parent=M, tree=tree)

# Calculate Max Independent Set Complexity O(n)
def maxIndependentSetTree(tree):
    IndependentSet = []
    while tree.leafs:
        leaf = (next(iter(tree.leafs)))
        IndependentSet.append(leaf)
        if leaf.parent != None:
            if leaf.parent.parent != None:
                leaf.parent.parent.children.remove(leaf.parent)
                if leaf.parent.parent.is_leaf() == True:
                    tree.leafs.add(leaf.parent.parent)
                leaf.parent.parent = None
            leaf.parent = None
        tree.leafs.remove(leaf)
    return IndependentSet

independent_set = maxIndependentSetTree(tree)
for temp in independent_set:
    print(temp.data)
