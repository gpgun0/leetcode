class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(x, y, index, visited):
            visited[x][y] = True
            if board[x][y] != word[index]:
                return False
            
            if index + 1 == len(word):
                return True

            for dx, dy in move:
                nx, ny = x+dx, y+dy

                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if dfs(nx, ny, index+1, visited):
                        return True
                    visited[nx][ny] = False


        for x in range(m):
            for y in range(n):
                visited = [[False]*n for _ in range(m)]
                if dfs(x, y, 0, visited):
                    return True

        return False