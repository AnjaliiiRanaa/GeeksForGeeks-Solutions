'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def preOrder(self, root):
        ans = []

        def solve(node):
            if node is None:
                return

            ans.append(node.data)      # Root
            solve(node.left)           # Left
            solve(node.right)          # Right

        solve(root)
        return ans
    