'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrder(self, root):
        ans = []

        def solve(node):
            if node is None:
                return

            solve(node.left)
            ans.append(node.data)
            solve(node.right)

        solve(root)
        return ans