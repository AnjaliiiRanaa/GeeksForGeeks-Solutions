class Solution:
    def isPalindrome(self, n):

        n = abs(n)
        original = n

        def reverse(num, rev):
            if num == 0:
                return rev

            return reverse(num // 10, rev * 10 + num % 10)

        return reverse(n, 0) == original