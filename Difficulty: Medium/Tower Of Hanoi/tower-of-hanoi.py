class Solution:
    def towerOfHanoi(self, n, fromm, to, aux):

        # Base Case
        if n == 1:
            return 1

        # Main Logic
        left = self.towerOfHanoi(n - 1, fromm, aux, to)
        right = self.towerOfHanoi(n - 1, aux, to, fromm)

        return left + 1 + right