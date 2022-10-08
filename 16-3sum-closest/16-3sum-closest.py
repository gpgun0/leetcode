class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        lnth = len(nums)
        ans, dis = None, float('inf')
        for i in range(lnth):
            start, end = i + 1, lnth - 1

            while end > start:
                Sum = nums[i] + nums[start] + nums[end]

                diff = abs(target - Sum)
                if diff < dis:
                    dis = diff
                    ans = Sum

                if target == Sum:
                    break
                elif Sum < target:
                    start += 1
                else:
                    end -= 1

        return ans