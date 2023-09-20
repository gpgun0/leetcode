class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int n = nums.size();
        int answer = -1;
        int sum = reduce(nums.begin(), nums.end(), 0);
        int target = sum-x;
        int left = 0;

        int curSum = 0;
        for (int right=0; right<n; right++) {
            curSum += nums[right];
            
            while (left <= right && curSum > target) {
                curSum -= nums[left];
                left++;
            }

            if (curSum == target) {
                answer = max(answer, right-left+1);
            }
        }

        return answer == -1 ? -1: n-answer;
    }
};