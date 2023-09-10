class Solution {
public:
    vector<vector<int>> answer;
    vector<int> path;

    void dfs(int n, vector<int>& path, vector<int>& nums) {
        if (path.size() == n) {
            answer.push_back(path);
            return;
        }

        for (int i=0; i<n; i++) {
            if (find(path.begin(), path.end(), nums[i]) == path.end()) {
                path.push_back(nums[i]);
                dfs(n, path, nums);
                path.pop_back();
            }
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        int n = nums.size();
        dfs(n, path, nums);
        return answer;
    }
};