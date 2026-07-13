class Solution:
    def factorial(self, n: int) -> int:
        # Base Case
        if n == 1 or n == 0:
            return 1

        # Main Logic
        val = self.factorial(n - 1)
        return n * val