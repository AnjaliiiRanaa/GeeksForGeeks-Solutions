'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def binaryTreeToBST(self, root):

        arr = []

        # Step 1: Store inorder values
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.data)
            inorder(node.right)

        inorder(root)

        # Step 2: Sort values
        arr.sort()

        i = 0

        # Step 3: Fill sorted values back
        def fill(node):
            nonlocal i

            if not node:
                return

            fill(node.left)

            node.data = arr[i]
            i += 1

            fill(node.right)

        fill(root)

        return root