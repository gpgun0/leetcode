class Solution {
public:
    vector<vector<int>> answer;
    int destination;
    vector<int> path = {0};

    void dfs(vector<vector<int>>& graph, int curNode, vector<int>& path) {
        if (curNode == destination) {
            answer.push_back(path);
            return;
        }

        for (auto nextNode :graph[curNode]) {
            path.push_back(nextNode);
            dfs(graph, nextNode, path);
            path.pop_back();
        }
        return;
    }

    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        destination = graph.size() - 1;

        dfs(graph, 0, path);

        return answer;
    }
};