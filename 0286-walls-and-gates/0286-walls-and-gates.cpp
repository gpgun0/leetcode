class Solution {
public:
    int INF = 2147483647;
    set<pair<int, int>> seen;
    vector<pair<int, int>> moves = {
        {-1, 0},
        {1, 0},
        {0, -1},
        {0, 1}
    };

    void wallsAndGates(vector<vector<int>>& rooms) {
        int m = rooms.size(), n = rooms[0].size();
        queue<tuple<int, int, int>> q;

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (rooms[i][j] == 0) {
                    q.push(make_tuple(i, j, 0));
                    seen.insert(make_pair(i, j));
                }
            }
        }

        while (!q.empty()) {
            tuple<int, int, int> cur = q.front();
            int x = get<0>(cur), y = get<1>(cur), cnt = get<2>(cur);
            q.pop();

            for (auto move: moves) {
                int dx = move.first, dy = move.second;
                int nx = x+dx, ny = y+dy;

                if (0 <= nx && nx < m && 0 <= ny && ny < n) {
                    if (!seen.count(make_pair(nx, ny)) && rooms[nx][ny] != -1) {
                        seen.insert(make_pair(nx, ny));
                        rooms[nx][ny] = cnt+1;
                        q.push(make_tuple(nx, ny, cnt+1));
                    }
                }
            }
        }
    }
};