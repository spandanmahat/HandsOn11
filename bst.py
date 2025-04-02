class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None

    def search(self, x, key):
        if x is None or key == x.key:
            return x
        if key < x.key:
            return self.search(x.left, key)
        else:
            return self.search(x.right, key)

    def insert(self, key):
        node = Node(key)
        y = None
        x = self.root
        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def delete(self, z):
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

tree = BST()

#showing that insert, search and delete work
tree.insert(15)
tree.insert(6)
tree.insert(18)
tree.insert(3)
tree.insert(7)

print("Search 7:", tree.search(tree.root, 7).key if tree.search(tree.root, 7) else "Not Found")
tree.delete(tree.search(tree.root, 6))

print("After deleting 6, search 6:", tree.search(tree.root, 6))

tree.insert(13)
print("Insert 13 and search 13:", tree.search(tree.root, 13).key)