class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> answer;
        map<int, int> dict;
        
        for (int i=0; i<nums.size(); i++) {
            if (dict[nums[i]]) {
                dict[nums[i]] += 1;
            } else {
                dict[nums[i]] = 1;
            }
        }

        for (auto iter=dict.begin(); iter!=dict.end(); iter++) {
            if (iter->second > nums.size()/3) {
                answer.push_back(iter->first);
            }
        }

        return answer;
    }
};