class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []
        board = ["."*n] * n
        verticals = [False] * n 

        def checkDiagonal(board, x, y):
            i, j = x+1, y+1
            while i < n and j < n:
                if board[i][j] == "Q":
                    return False
                i += 1
                j += 1

            i, j = x-1, y+1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1    

            i, j = x-1, y-1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            i, j = x+1, y-1
            while i < n and j >= 0:
                if board[i][j] == "Q":
                    return False
                i += 1
                j -= 1

            return True            


        def dfs(board, x, y):
            if x == n:
                output.append(board[:])
                return

            for y in range(n):
                if verticals[y]:
                    continue
                if not checkDiagonal(board, x, y):
                    continue
                
                temp = ["."]*n
                temp[y] = "Q"
                board[x] = "".join(temp)
                verticals[y] = True

                dfs(board, x+1, 0)

                verticals[y] = False
                board[x] = "." * n

        dfs(board, 0, 0)

        return output