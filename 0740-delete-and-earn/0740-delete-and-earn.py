class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        dp = [0]*(max(nums)+1)
        
        for num in nums:
            dic[num] += 1
        
        for i in range(1, len(dp)):
            if i == 1:
                dp[i] = dic[1] * 1
            
            else:
                dp[i] = max(dp[i-1], dic[i]*i + dp[i-2])
        
        return dp[-1]