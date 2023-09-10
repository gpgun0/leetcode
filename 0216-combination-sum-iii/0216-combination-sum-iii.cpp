class Solution {
public:
    vector<vector<int>> answer;
    vector<int> path;

    void dfs(int remain, int k, int start, vector<int> path) {
        if (k == 0) {
            if (remain == 0) {
                answer.push_back(path);
                return;
            }
            return;
        }

        for (int i=start; i<10; i++) {
            path.push_back(i);
            
            if (remain-i < 0) {
                return;
            }
            dfs(remain-i, k-1, i+1, path);
            path.pop_back();
        }

    }

    vector<vector<int>> combinationSum3(int k, int n) {
        
        dfs(n, k, 1, path);

        return answer;
    }
};