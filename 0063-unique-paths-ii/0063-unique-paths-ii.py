class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[-1][-1]:
            return 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue

                if i == 0 and j == 0:
                    obstacleGrid[i][j] = -1

                elif i == 0 and obstacleGrid[i][j-1] != 1:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]

                elif j == 0 and obstacleGrid[i-1][j] != 1:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = min(0, obstacleGrid[i-1][j]) + min(0, obstacleGrid[i][j-1])

        return -obstacleGrid[-1][-1]