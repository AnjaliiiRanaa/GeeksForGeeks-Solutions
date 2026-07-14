class Solution:
    def subsetSums(self, arr):

        ans = []

        def backtrack(i, curr_sum):

            if i == len(arr):
                ans.append(curr_sum)
                return

            # Include
            backtrack(i + 1, curr_sum + arr[i])

            # Exclude
            backtrack(i + 1, curr_sum)

        backtrack(0, 0)

        return sorted(ans)