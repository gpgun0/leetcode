class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        map<int, vector<int>> graph;
        vector<bool> seen(n, 0);
        queue<int> q;

        for (auto edge: edges) {
            int u = edge[0], v = edge[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        q.push(source);
        seen[source] = 1;

        while (!q.empty()) {
            int curNode = q.front();
            q.pop();
            if (curNode == destination) {
                return true;
            }

            for (auto nextNode: graph[curNode]) {
                if (seen[nextNode]) {
                    continue;
                }

                seen[nextNode] = 1;
                q.push(nextNode);
            }
        }

        return false;
    }
};