'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''


class Solution:
    def search(self, root, x):
        if root is None:
            return False

        if root.data == x:
            return True

        if x < root.data:
            return self.search(root.left, x)

        return self.search(root.right, x)