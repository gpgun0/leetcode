class Solution {
public:
    vector<vector<int>> answer;
    vector<int> path;
    map<int, int> counter;
    vector<vector<int>> counterList;

    void dfs(int remain, vector<int>& path, int start, vector<int>& candidates) {
        if (remain == 0) {
            answer.push_back(path);
            return;
        }
        if (remain < 0) {
            return;
        }

        for (int i=start; i<counterList.size(); i++) {
            vector<int> entry = counterList[i];

            if (entry[1] <= 0) {
                continue;
            }

            counterList[i] = {entry[0], entry[1]-1};
            path.push_back(entry[0]);
            dfs(remain-entry[0], path, i, candidates);
            path.pop_back();
            counterList[i] = {entry[0], entry[1]};
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        for (int i=0; i<candidates.size(); i++) {
            counter[candidates[i]]++;
        }
        
        for (auto& entry : counter) {
            counterList.push_back({entry.first, entry.second});
        }

        dfs(target, path, 0, candidates);

        return answer;
    }
};