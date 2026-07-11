class Solution:
    def missingNum(self, arr):
        n = len(arr) + 1

        xor1 = 0
        xor2 = 0

        for i in range(1, n + 1):
            xor1 ^= i

        for num in arr:
            xor2 ^= num

        return xor1 ^ xor2