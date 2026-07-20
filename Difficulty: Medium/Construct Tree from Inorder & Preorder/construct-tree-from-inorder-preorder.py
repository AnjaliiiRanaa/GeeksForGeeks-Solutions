'''  Structure of a Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
class Solution:
    def buildTree(self, inorder, preorder):
        
        mp = {}
        for i in range(len(inorder)):
            mp[inorder[i]] = i

        self.preIndex = 0

        def solve(start, end):
            if start > end:
                return None

            rootVal = preorder[self.preIndex]
            self.preIndex += 1

            root = Node(rootVal)

            idx = mp[rootVal]

            root.left = solve(start, idx - 1)
            root.right = solve(idx + 1, end)

            return root

        return solve(0, len(inorder) - 1)