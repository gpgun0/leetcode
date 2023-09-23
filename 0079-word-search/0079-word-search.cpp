class Solution {
public:
    vector<pair<int, int>> moves = {
        {-1, 0},
        {1, 0},
        {0, -1},
        {0, 1}
    };
    set<pair<int, int>> seen;

    bool dfs(string path, int x, int y, int idx, vector<vector<char>> board, string word) {
        if (path.length() > word.length()) {
            return false;
        }
        if (path == word) {
            return true;
        }

        bool flag = false;
        for (auto move: moves) {
            int dx = move.first, dy = move.second;
            int nx = x+dx, ny = y+dy;

            if (0 > nx or nx >= board.size() or 0 > ny or ny >= board[0].size()) {
                continue;
            }
            if (board[nx][ny] == word[idx] && !seen.count({nx, ny})) {
                seen.insert(make_pair(nx, ny));
                flag = dfs(path + board[nx][ny], nx, ny, idx+1, board, word);
                seen.erase(make_pair(nx, ny));
                if (flag) {
                    return true;
                }
            }
        }

        return flag;
    }

    bool exist(vector<vector<char>>& board, string word) {
        set<char> s;
        for (int i=0; i<board.size(); i++) {
            for (int j=0; j<board[0].size(); j++) {
                if (!s.count(board[i][j])) {
                    s.insert(board[i][j]);
                }
            }
        }

        for (auto c: word) {
            if (!s.count(c)) {
                return false;
            }
        }
        
        seen.clear();
        for (int i=0; i<board.size(); i++) {
            for (int j=0; j<board[0].size(); j++) {
                string path = "";

                if (board[i][j] == word[0]) {
                    seen.insert({i, j});
                    if (dfs(path + word[0], i, j, 1, board, word)) {
                        return true;
                    }
                    seen.clear();
                }
            }
        }

        return false;
    }
};