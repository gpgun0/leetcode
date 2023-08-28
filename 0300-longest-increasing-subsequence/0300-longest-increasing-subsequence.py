class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [nums[0]]
        
        dp = [1]*n

        for i in range(1, n):
            if nums[i] > lis[-1]:
                lis.append(nums[i])
            else:
                j = 0
                while j < len(lis):
                    if nums[i] <= lis[j]:
                        lis[j] = nums[i]
                        break
                    j += 1

        return len(lis)