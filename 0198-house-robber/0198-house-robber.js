/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    dp = Array(nums.length).fill(0)
    
    dp[0] = nums[0]

    for (let i = 1; i < nums.length; i++) {
        if (i == 1) {
            dp[i] = Math.max(dp[i-1], nums[i]);
        } else {
            dp[i] = Math.max(dp[i-1], nums[i] + dp[i-2]);
        }
    }

    return Math.max(...dp);
};