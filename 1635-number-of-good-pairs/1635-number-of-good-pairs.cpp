class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        map<int, int> count;
        int ans = 0;
        
        for (auto num: nums) {
            if (count[num]) {
                count[num] += 1;
            } else {
                count[num] = 1;
            }
        }

        for (auto it=count.begin(); it!=count.end(); it++) {
            ans += (it->second)*(it->second-1)/2;
        }

        return ans;
    }
};