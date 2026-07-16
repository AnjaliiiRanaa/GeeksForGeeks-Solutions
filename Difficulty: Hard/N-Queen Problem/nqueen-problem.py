class Solution:
    def nQueen(self, n):

        board = [[0] * n for _ in range(n)]
        ans = []

        def isSafe(row, col):

            # same column
            for i in range(row):
                if board[i][col]:
                    return False

            # left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j]:
                    return False
                i -= 1
                j -= 1

            # right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j]:
                    return False
                i -= 1
                j += 1

            return True

        def solve(row, path):

            if row == n:
                ans.append(path[:])
                return

            for col in range(n):

                if isSafe(row, col):

                    board[row][col] = 1
                    path.append(col + 1)      # GFG uses 1-based columns

                    solve(row + 1, path)

                    path.pop()
                    board[row][col] = 0

        solve(0, [])

        return ans