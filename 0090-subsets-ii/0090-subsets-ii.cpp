class Solution {
public:
    int startIdx;
    vector<vector<int>> subsets = {{}};
    int subsetsSize = 0;

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        for (int i=0; i<nums.size(); i++) {
            startIdx = (i>0 && nums[i] == nums[i-1]) ? subsetsSize : 0;
            subsetsSize = subsets.size();

            for (int j=startIdx; j<subsetsSize; j++) {
                vector<int> newSubset = subsets[j];
                newSubset.push_back(nums[i]);
                subsets.push_back(newSubset);
            }
        }

        return subsets;
    }
};