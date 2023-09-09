class Solution {
public:
    vector<vector<int>> answer;
    vector<int> path;

    void dfs(int remain, vector<int>& path, int start, vector<int>& candidates) {
        if (remain == 0) {
            answer.push_back(path);
            return;
        }

        for (int i=start; i<candidates.size(); i++) {
            if (i > start && candidates[i-1] == candidates[i]) {
                continue;
            }
            if (remain-candidates[i] < 0) {
                break;
            }

            path.push_back(candidates[i]);
            dfs(remain-candidates[i], path, i+1, candidates);
            path.pop_back();
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        dfs(target, path, 0, candidates);

        return answer;
    }
};