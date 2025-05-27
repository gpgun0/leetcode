class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        hash_map = defaultdict(bool)

        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if hash_map[board[i][j]]:
                    return False
                hash_map[board[i][j]] = True
            
            hash_map.clear()

        for i in range(n):
            for j in range(n):
                if board[j][i] == ".":
                    continue
                if hash_map[board[j][i]]:
                    return False
                hash_map[board[j][i]] = True

            hash_map.clear()
        
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                for l in range(i, i+3):
                    for k in range(j, j+3):
                        if board[l][k] == ".":
                            continue
                        if hash_map[board[l][k]]:
                            return False
                        hash_map[board[l][k]] = True
                    
                hash_map.clear()
        
        return True

