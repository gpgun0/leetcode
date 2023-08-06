class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l = len(nums)
        result = [0]*l
        result[0] = nums[0]
        
        for i in range(1, l):
            result[i] = result[i-1] + nums[i]
        
        return result