class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        map<int, vector<int>> graph;
        queue<int> q;
        vector<bool> seen(n);

        for (auto edge: edges) {
            int u = edge[0], v = edge[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        seen[source] = true;
        q.push(source);

        while (!q.empty()) {
            int curNode = q.front();
            q.pop();

            if (curNode == destination) {
                return true;
            }
            for (auto nextNode: graph[curNode]) {
                if (!seen[nextNode]) {
                    seen[nextNode] = true;
                    q.push(nextNode);
                }
            }
        }

        return false;
    }
};