class Solution {
public:
    vector<vector<int>> answer;
    vector<int> path;

    void dfs(vector<int>& path, vector<int>& nums, int start) {
        answer.push_back(path);
        
        for (int i=start; i<nums.size(); i++) {
            path.push_back(nums[i]);
            dfs(path, nums, i+1);
            path.pop_back();
        }
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        dfs(path, nums, 0);
        return answer;
    }
};