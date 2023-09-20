class Solution {
public:
    set<char> horizontalSet[9];
    set<char> verticalSet[9];
    set<char> gridSet[9];

    bool dfs(int row, int col, vector<vector<char>>& board) {
        if (row == 9) {
            return true;
        }

        if (board[row][col] != '.') {
            if (col < 8) {
                return dfs(row, col+1, board);
            } else {
                return dfs(row+1, 0, board);
            }
        }
        bool flag = false;

        for (int i=1; i<10; i++) {
            char c = i + '0';
            int gridIndex = (row/3)*3 + col/3;

            if (horizontalSet[row].count(c) || verticalSet[col].count(c)
                || gridSet[gridIndex].count(c)) {
                continue;
            }

            board[row][col] = c;
            horizontalSet[row].insert(c);
            verticalSet[col].insert(c);
            gridSet[gridIndex].insert(c);
            if (col < 8) {
                flag = dfs(row, col+1, board);
            } else {
                flag = dfs(row+1, 0, board);
            }

            gridSet[gridIndex].erase(c);
            verticalSet[col].erase(c);
            horizontalSet[row].erase(c);
            if (!flag) {
                board[row][col] = '.';
            }
            if (flag) {
                break;
            }
        }

        return flag;
    }

    void solveSudoku(vector<vector<char>>& board) {

        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) {
                if (board[i][j] != '.') {
                    horizontalSet[i].insert(board[i][j]);
                    verticalSet[j].insert(board[i][j]);
                    gridSet[(i/3)*3 + j/3].insert(board[i][j]);
                }
            }
        }

        dfs(0, 0, board);
    }
};