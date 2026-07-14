class Solution:
    def subsets(self, arr):

        ans = []

        def backtrack(i, subset):

            if i == len(arr):
                ans.append(subset[:])
                return

            # Include
            subset.append(arr[i])
            backtrack(i + 1, subset)

            # Backtrack
            subset.pop()

            # Exclude
            backtrack(i + 1, subset)

        backtrack(0, [])

        return ans