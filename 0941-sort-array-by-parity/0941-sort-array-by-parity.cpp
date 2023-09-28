class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int l = 0, r = nums.size()-1;
        while (l <= r) {

            while (nums[l]%2 != 1 && l < r) {
                l += 1;
            }

            while (nums[r]%2 != 0 && l < r) {
                r -= 1;
            }
            int temp = nums[r];
            nums[r] = nums[l];
            nums[l] = temp;
            l += 1;
            r -= 1;
        }

        return nums;
    }
};