class Solution {
public:
    bool dfs(map<int, vector<int>>& graph, vector<bool>& seen, int curNode, int destination) {
        if (curNode == destination) {
            return true;
        }
        if (seen[curNode]) {
            return false;
        }

        seen[curNode] = true;
        for (auto nextNode: graph[curNode]) {
            if (dfs(graph, seen, nextNode, destination)) {
                return true;
            }
        }

        return false;
    }
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        map<int, vector<int>> graph;
        vector<bool> seen(n);

        for (auto edge: edges) {
            int u = edge[0], v = edge[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        return dfs(graph, seen, source, destination);
    }
};