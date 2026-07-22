'''Structure of a Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def kthLargest(self, root, k):

        self.count = 0
        self.ans = -1

        def reverseInorder(node):
            if not node or self.count >= k:
                return

            reverseInorder(node.right)

            self.count += 1

            if self.count == k:
                self.ans = node.data
                return

            reverseInorder(node.left)

        reverseInorder(root)

        return self.ans