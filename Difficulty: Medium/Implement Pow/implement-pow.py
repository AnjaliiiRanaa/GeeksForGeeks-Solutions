class Solution:
    def power(self, b: float, e: int) -> float:

        def fastPow(base, exp):
            if exp == 0:
                return 1

            half = fastPow(base, exp // 2)

            if exp % 2 == 0:
                return half * half
            else:
                return base * half * half

        if e < 0:
            return 1 / fastPow(b, -e)

        return fastPow(b, e)