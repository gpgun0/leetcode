class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num = nums[0]
        idx = 1

        for i in range(1, len(nums)):
            if num != nums[i]:
                nums[idx] = nums[i]
                idx += 1
                num = nums[i]
        
        return idx