class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}

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

            if right - left == 2 or right - left == 3:
                memo[key] = check(left, right)
                return memo[key]
            
            if isValidate(left, left+2) and isValidate(left+2, right):
                memo[key] = True
                return memo[key]

            elif isValidate(left, left+3) and isValidate(left+3, right):
                memo[key] = True
                return memo[key]
            else:
                memo[key] = False
                return memo[key]

        isValidate(0, n)
        print(memo)

        return isValidate(0, n)