# Definition for Node
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def inOrder(self, root):

        stack = []
        ans = []
        curr = root

        while curr or stack:

            # Push all left nodes
            while curr:
                stack.append(curr)
                curr = curr.left

            # Visit node
            curr = stack.pop()
            ans.append(curr.data)

            # Move to right subtree
            curr = curr.right

        return ans