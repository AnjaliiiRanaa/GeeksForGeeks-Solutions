class Solution:
    def targetSumComb(self, arr, target):

        ans = []

        def backtrack(i, target, path):

            if target == 0:
                ans.append(path[:])
                return

            if i == len(arr) or target < 0:
                return

            # Take current element
            path.append(arr[i])
            backtrack(i, target - arr[i], path)

            # Backtrack
            path.pop()

            # Don't take current element
            backtrack(i + 1, target, path)

        backtrack(0, target, [])

        return ans