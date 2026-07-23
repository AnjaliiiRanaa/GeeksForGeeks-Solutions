'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def postOrder(self, root):

        if not root:
            return []

        stack1 = [root]
        stack2 = []
        ans = []

        while stack1:

            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)

            if node.right:
                stack1.append(node.right)

        while stack2:
            ans.append(stack2.pop().data)

        return ans