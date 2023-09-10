class Solution {
public:
    vector<vector<int>> answer;
    vector<int> path;

    vector<vector<int>> subsets(vector<int>& nums) {
        answer.push_back(vector<int>());

        for (int num: nums) {
            vector<vector<int>> newSubset;
            
            for (vector<int> subset: answer) {
                subset.push_back(num);
                newSubset.push_back(subset);
            }

            for (vector<int> subset: newSubset) {
                answer.push_back(subset);
            }
        }
        
        return answer;
    }
};