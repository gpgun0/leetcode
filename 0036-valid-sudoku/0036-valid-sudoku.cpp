class Solution {
public:
    set<int> rows[9];
    set<int> columns[9];
    set<int> boxes[9];

    bool isValidSudoku(vector<vector<char>>& board) {
        
        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) {
                int num = board[i][j];
                
                if (num == '.') {
                    continue;
                }

                if (rows[i].count(num) || columns[j].count(num) || boxes[(i/3)*3 + j/3].count(num)) {
                    return false;
                }

                rows[i].insert(num);
                columns[j].insert(num);
                boxes[(i/3)*3 + j/3].insert(num);
            }
        }

        return true;
    }
};