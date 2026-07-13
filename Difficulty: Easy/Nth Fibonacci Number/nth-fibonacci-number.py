class Solution:
    def nthFibonacci(self, n):

        # Base Cases
        if n == 0:
            return 0
        if n == 1:
            return 1

        # Main Logic
        val1 = self.nthFibonacci(n - 1)
        val2 = self.nthFibonacci(n - 2)

        return val1 + val2