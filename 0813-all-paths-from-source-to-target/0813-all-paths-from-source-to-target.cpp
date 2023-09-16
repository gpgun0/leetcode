class Solution {
public:
    vector<vector<int>> answer;
    int destination;
    set<int> seen;
    queue<vector<int>> q;

    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        destination = graph.size() - 1;
        
        q.push({ 0 });
        
        while (!q.empty()) {
            vector<int> path = q.front();
            q.pop();
            int curNode = path.back();

            for (auto nextNode: graph[curNode]) {
                path.push_back(nextNode);
                if (nextNode == destination) {
                    answer.push_back(path);
                }
                if (!seen.count(nextNode)) {
                    q.push(path);
                }
                
                path.pop_back();
            }
        }
        return answer;
    }
};