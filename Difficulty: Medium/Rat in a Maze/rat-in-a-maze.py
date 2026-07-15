class Solution:
    def ratInMaze(self, maze):
        n = len(maze)
        ans = []

        if maze[0][0] == 0:
            return ans

        visited = [[False] * n for _ in range(n)]

        directions = [
            (1, 0, "D"),
            (0, -1, "L"),
            (0, 1, "R"),
            (-1, 0, "U")
        ]

        def dfs(i, j, path):
            if i == n - 1 and j == n - 1:
                ans.append(path)
                return

            visited[i][j] = True

            for di, dj, move in directions:
                ni = i + di
                nj = j + dj

                if (0 <= ni < n and
                    0 <= nj < n and
                    maze[ni][nj] == 1 and
                    not visited[ni][nj]):
                    dfs(ni, nj, path + move)

            visited[i][j] = False

        dfs(0, 0, "")
        return ans