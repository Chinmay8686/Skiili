
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.cnt = 0

    # Insert a node
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if new_node.data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                temp = temp.right

    # Delete a node
    def del_node(self, rt, val):
        if rt is None:
            return None

        if val < rt.data:
            rt.left = self.del_node(rt.left, val)

        elif val > rt.data:
            rt.right = self.del_node(rt.right, val)

        else:
            if rt.left is None:
                return rt.right

            if rt.right is None:
                return rt.left

            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.del_node(rt.right, succ.data)

        return rt

    # Find inorder successor
    def get_successor(self, temp):
        temp = temp.right

        while temp.left is not None:
            temp = temp.left

        return temp

    # Inorder Traversal
    def inorder(self, rt):
        if rt is None:
            return

        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    # Count leaf nodes
    def count_leaf(self, rt):
        if rt is None:
            return

        self.count_leaf(rt.left)

        if rt.left is None and rt.right is None:
            self.cnt += 1

        self.count_leaf(rt.right)

    # Preorder Traversal
    def preorder(self, rt):
        if rt is None:
            return

        print(rt.data, end=" ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    # Postorder Traversal
    def postorder(self, rt):
        if rt is None:
            return

        self.postorder(rt.left)
        self.postorder(rt.right)
        print(rt.data, end=" ")

    # Search a node
    def search(self, key):
        temp = self.root

        while temp:
            if temp.data == key:
                return True

            elif key < temp.data:
                temp = temp.left

            else:
                temp = temp.right

        return False

    # Find minimum and maximum
    def findminmax(self):
        if self.root is None:
            print("\nTree is empty")
            return

        temp = self.root

        while temp.left:
            temp = temp.left

        print("\nMin:", temp.data)

        temp = self.root

        while temp.right:
            temp = temp.right

        print("Max:", temp.data)


# Driver Code
b1 = BST()

for val in [100, 10, 450, 4, 65, 300, 500]:
    b1.insert(Node(val))

print("Inorder:")
b1.inorder(b1.root)

print("\n\nPreorder:")
b1.preorder(b1.root)

print("\n\nPostorder:")
b1.postorder(b1.root)

print()
b1.findminmax()

# Delete node
b1.root = b1.del_node(b1.root, 65)

print("\nAfter Delete:")
b1.inorder(b1.root)

# Count leaf nodes
b1.cnt = 0
b1.count_leaf(b1.root)

print("\nTotal no of leaf nodes:", b1.cnt)

# Search node
if b1.search(50):
    print("\nFound the node")
else:
    print("\nNot found")
