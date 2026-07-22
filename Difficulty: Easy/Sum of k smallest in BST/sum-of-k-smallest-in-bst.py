'''
# Structure of a Tree Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def sum(self, root, k):

        self.count = 0
        self.ans = 0

        def inorder(node):
            if not node or self.count >= k:
                return

            inorder(node.left)

            if self.count < k:
                self.ans += node.data
                self.count += 1

            inorder(node.right)

        inorder(root)

        return self.ans