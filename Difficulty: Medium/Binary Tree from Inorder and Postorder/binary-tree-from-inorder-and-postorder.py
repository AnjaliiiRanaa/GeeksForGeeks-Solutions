""" Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
"""


class Solution:
    def buildTree(self, inorder, postorder):

        mp = {}
        for i in range(len(inorder)):
            mp[inorder[i]] = i

        self.postIndex = len(postorder) - 1

        def solve(start, end):

            if start > end:
                return None

            rootVal = postorder[self.postIndex]
            self.postIndex -= 1

            root = Node(rootVal)

            idx = mp[rootVal]

            # IMPORTANT
            root.right = solve(idx + 1, end)
            root.left = solve(start, idx - 1)

            return root

        return solve(0, len(inorder) - 1)       