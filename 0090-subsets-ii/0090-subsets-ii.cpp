class Solution {
public:
    vector<vector<int>> answer;
    map<int, int> counter;
    vector<vector<int>> counterList;
    vector<int> path;

    void dfs(vector<int> path, vector<int>& nums, int start) {
        answer.push_back(path);
        
        for (int i=start; i<counterList.size(); i++) {
           vector<int> entry = counterList[i];
           int value = entry[0], count = entry[1];

           if (count <= 0) {
               continue;
           }

            counterList[i] = {value, count-1};
            path.push_back(value);
            dfs(path, nums, i);
            path.pop_back();
            counterList[i] = {value, count};
        }
        return;
    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        for (int num: nums) {
            counter[num]++;
        }

        for (auto& [key, value]: counter) {
            counterList.push_back({key, value});
        }

        dfs(vector<int>(), nums, 0);
        return answer;
    }
};