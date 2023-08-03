class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [0] + nums
        
        dp = [-10**4]*(n+1)
        
        for i in range(1, n+1):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        return max(dp)