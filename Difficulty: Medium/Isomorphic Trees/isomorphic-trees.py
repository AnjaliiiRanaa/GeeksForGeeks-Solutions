'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''


class Solution:
    def isIsomorphic(self, r1, r2):

        # Dono empty
        if r1 is None and r2 is None:
            return True

        # Ek empty
        if r1 is None or r2 is None:
            return False

        # Data different
        if r1.data != r2.data:
            return False

        # Case 1: No Swap
        noSwap = (self.isIsomorphic(r1.left, r2.left) and
                  self.isIsomorphic(r1.right, r2.right))

        # Case 2: Swap
        swap = (self.isIsomorphic(r1.left, r2.right) and
                self.isIsomorphic(r1.right, r2.left))

        return noSwap or swap