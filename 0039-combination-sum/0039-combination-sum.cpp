class Solution {
public:
    int getSum(vector<int>& arr) {
        int result = 0;

        for (int num:arr) {
            result += num;
        }

        return result;
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> answer;
        vector<int> path;

        function<void(vector<int>&path, int)> dfs = [&](vector<int> path, int start) {
            int sum = getSum(path);
            if (sum == target) {
                answer.push_back(path);
                return;
            }

            if (sum > target) {
                return;
            }

            for (int i=start; i<candidates.size(); i++) {
                path.push_back(candidates[i]);
                dfs(path, i);
                path.pop_back();
            }
        };

        dfs(path, 0);

        return answer;
    }
};