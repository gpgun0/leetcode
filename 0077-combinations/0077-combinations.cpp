class Solution {
public:
    vector<vector<int>> answer;
    vector<int> path;

    void backtrack(vector<int>& path, int n, int k, int s) {
        if (path.size() == k) {
            answer.push_back(path);
            return;
        }

        for (int i=s; i<=n; i++) {
            path.push_back(i);
            backtrack(path, n, k, i+1);
            path.pop_back();
        }

        return;
    }

    vector<vector<int>> combine(int n, int k) {
        backtrack(path, n, k, 1);

        return answer;
    }
};