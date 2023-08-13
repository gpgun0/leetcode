class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        nums = [0] + nums
        n = len(nums)
        dp = [0]*n
        dp[0] = 1

        for i in range(1, n):
            if i >= 2 and nums[i] == nums[i-1]:
                dp[i] |= dp[i-2]
            if i >= 3 and nums[i] == nums[i-1] == nums[i-2]:
                dp[i] |= dp[i-3]
            if i >= 3 and nums[i] == nums[i-1]+1 == nums[i-2]+2:
                dp[i] |= dp[i-3]

        return dp[-1]
            
        def check(left, right):
            if right - left == 2:
                if nums[left] == nums[right-1]:
                    return True
                else:
                    return False
            
            if right - left == 3:
                if nums[left] == nums[left+1] and nums[left+1] == nums[right-1]:
                    return True
                if nums[left+1] - nums[left] == 1 and nums[right-1] - nums[left+1] == 1:
                    return True
                else:
                    return False
        
        def isValidate(left, right):
            key = f'{left}:{right}'

            if key in memo:
                return memo[key]

            if right - left <= 1:
                memo[key] = False
                return memo[key]

            if right - left <= 3:
                memo[key] = check(left, right)
                return memo[key]
            
            if isValidate(left, left+2) and isValidate(left+2, right):
                memo[key] = True

            elif isValidate(left, left+3) and isValidate(left+3, right):
                memo[key] = True

            else:
                memo[key] = False
            
            return memo[key]

        return isValidate(0, n)