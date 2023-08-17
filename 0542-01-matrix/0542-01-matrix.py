class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited = set()
        q = deque([])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    visited.add((i, j))

        while q:
            x, y, acc = q.popleft()

            for dx, dy in move:
                nx = x+dx
                ny = y+dy

                if 0 <= nx < m and 0 <= ny < n and \
                    (nx, ny) not in visited:
                    
                    mat[nx][ny] = acc+1
                    q.append((nx, ny, acc+1))
                    visited.add((nx, ny))

        return mat