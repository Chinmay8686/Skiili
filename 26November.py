
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # 1. Insert a node
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

    # 2. Search a token number
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

    # 3. Display tokens in sorted order
    def inorder(self, rt):
        if rt is None:
            return

        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    # 4. Find minimum and maximum
    def findminmax(self):
        if self.root is None:
            print("Tree is empty")
            return

        temp = self.root

        while temp.left:
            temp = temp.left

        print("Smallest token number:", temp.data)

        temp = self.root

        while temp.right:
            temp = temp.right

        print("Largest token number:", temp.data)

    # Find inorder successor
    def get_successor(self, temp):
        temp = temp.right

        while temp.left:
            temp = temp.left

        return temp

    # 5. Delete a token number
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


# Driver Code

b1 = BST()

# 1. Insert patient token numbers
tokens = [50, 30, 70, 20, 40, 60, 80, 10]

for val in tokens:
    b1.insert(Node(val))

print("Hospital Patient Token Management")

# 2. Search token number 40
if b1.search(40):
    print("\nToken 40 found")
else:
    print("\nToken 40 not found")

# 3. Display sorted token numbers
print("\nTokens in sorted order:")
b1.inorder(b1.root)

# 4. Find smallest and largest
print("\n")
b1.findminmax()

# 5. Delete token number 70
b1.root = b1.del_node(b1.root, 70)

print("\n\nAfter deleting token 70:")
b1.inorder(b1.root)
print()
