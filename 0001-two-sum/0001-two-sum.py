class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i in range(len(nums)):
            num = target-nums[i]
            if num in dic:
                return [i, dic[num]]

            dic[nums[i]] = i