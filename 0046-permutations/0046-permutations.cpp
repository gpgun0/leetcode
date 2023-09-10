class Solution {
public:
    vector<vector<int>> answer;
    vector<int> path;

    bool check(int num) {
        for (int i=0; i<path.size(); i++) {
            if (path[i] == num) {
                return false;
            }
        }
        return true;
    }

    void dfs(int n, vector<int>& path, vector<int>& nums) {
        if (path.size() == n) {
            answer.push_back(path);
            return;
        }

        for (int i=0; i<n; i++) {
            if (!check(nums[i])) continue;
            path.push_back(nums[i]);
            dfs(n, path, nums);
            path.pop_back();
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        int n = nums.size();
        dfs(n, path, nums);
        return answer;
    }
};