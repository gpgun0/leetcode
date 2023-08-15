class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = max(nums)
        arr = [0]*(n+1)
        dp = [0]*(n+1)

        for num in sorted(nums):
            arr[num] += num
        
        for i in range(1, len(dp)):
            if i == 1:
                dp[i] = arr[i]
            else:
                dp[i] = max(dp[i-1], arr[i] + dp[i-2])
        
        return max(dp)