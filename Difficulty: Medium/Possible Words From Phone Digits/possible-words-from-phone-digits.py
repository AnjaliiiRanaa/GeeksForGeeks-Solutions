class Solution:
    def possibleWords(self, arr):
        mp = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        ans = []

        def solve(i, path):

            if i == len(arr):
                ans.append(path)
                return

            digit = arr[i]

            if digit == 0 or digit == 1:
                solve(i + 1, path)
                return

            for ch in mp[digit]:
                solve(i + 1, path + ch)

        solve(0, "")
        return ans