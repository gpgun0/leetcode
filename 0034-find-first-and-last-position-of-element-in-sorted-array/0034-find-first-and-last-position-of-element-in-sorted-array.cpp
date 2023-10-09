class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if (nums.size() == 0) {
            return {-1, -1};
        }
        int l = 0, r = nums.size()-1;


        while (l <= r) {
            int mid = (l + r)/2;

            if (nums[mid] > target) {
                r = mid-1;
            } else if (nums[mid] < target) {
                l = mid+1;
            } else {
                l = mid;
                r = mid;
                break;
            }
        }

        if (l != r) {
            return {-1, -1};
        }

        while (l >= 0 && nums[l] == target) {
            l -= 1;
        }
        while (r < nums.size() && nums[r] == target) {
            r += 1;
        }

        return {l+1, r-1};
    }
};