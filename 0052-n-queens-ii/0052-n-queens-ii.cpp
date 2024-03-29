class Solution {
public:
    int count = 0;

    bool check(int row, int col, int n, vector<vector<int>>& board) {
        for (int i=0; i<row; i++) {
            if (i != row && board[i][col]) {
                return false;
            }
        }
        int i=row, j=col;
        while (i>0 && j>0) {
            if (board[--i][--j]) {
                return false;
            }
        }
        i=row, j=col;
        while (i>0 && j<n-1) {
            if (board[--i][++j]) {
                return false;
            }
        }
        return true;
    }

    void dfs(int row, int n, vector<vector<int>>& board) {
        if (row == n) {
            count += 1;
            return;
        }

        for (int col=0; col<n; col++) {
            if (check(row, col, n, board)) {
                board[row][col] = 1;
                dfs(row+1, n, board);
                board[row][col] = 0;
            }
        }

        return;
    }

    int totalNQueens(int n) {
        vector<vector<int>> board(n, vector<int>(n, 0));

        dfs(0, n, board);
        return count;
    }
};