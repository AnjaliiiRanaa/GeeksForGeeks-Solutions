'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def countPairs(self, root1, root2, x):

        s = set()

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            s.add(node.data)
            inorder(node.right)

        inorder(root1)

        ans = 0

        def search(node):
            nonlocal ans

            if not node:
                return

            search(node.left)

            if (x - node.data) in s:
                ans += 1

            search(node.right)

        search(root2)

        return ans