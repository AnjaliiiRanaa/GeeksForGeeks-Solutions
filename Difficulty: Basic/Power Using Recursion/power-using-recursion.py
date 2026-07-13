class Solution:
    def RecursivePower(self, n, p):

        # Base Case
        if p == 0:
            return 1

        # Main Logic
        val = self.RecursivePower(n, p - 1)

        return n * val