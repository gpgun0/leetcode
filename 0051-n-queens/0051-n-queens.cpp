class Solution {
public:
    vector<vector<string>> answer;
    set<int> antiDiagonals;
    set<int> diagonals;
    set<int> verticals;

    void backtrack(int row, int n, vector<string>& board) {
        if (row == n) {
            answer.push_back(board);
            return;
        }

        for (int col=0; col<n; col++) {
            if (antiDiagonals.count(row+col) || diagonals.count(row-col)
                || verticals.count(col)) {
                    continue;
                }

            antiDiagonals.insert(row+col);
            diagonals.insert(row-col);
            verticals.insert(col);
            board[row][col] = 'Q';
            
            backtrack(row+1, n, board);

            board[row][col] = '.';
            verticals.erase(col);
            diagonals.erase(row-col);
            antiDiagonals.erase(row+col);
        }

        return;
    }

    vector<vector<string>> solveNQueens(int n) {
        vector<string> board;
        string dots;

        for (int i=0; i<n; i++) {
            dots += ".";
        }
        for (int i=0; i<n; i++) {
            board.push_back(dots);
        }

        backtrack(0, n, board);
        return answer;
    }
};