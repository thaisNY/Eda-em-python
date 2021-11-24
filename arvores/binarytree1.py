class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data):# a raiz é suficiente para definir a arvore
        node = TreeNode(data)
        self.root = node

Tree = BinaryTree(7)
Tree.root.left = TreeNode(18)
Tree.root.right = TreeNode(14)

print(Tree.root)
print(Tree.root.left)
print(Tree.root.right)



