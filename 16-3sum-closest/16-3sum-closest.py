class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        result = nums[0]+nums[1]+nums[2]
        dis = 10001
        
        for std in range(n-2):
            left = std+1
            right = n-1
            
            if std > 0 and nums[std] == nums[std-1]:
                continue
            
            while left < right:
                if left > std+1 and nums[left] == nums[left-1]:
                    left += 1
                    continue
                if right < n-1 and nums[right] == nums[right+1]:
                    right -= 1
                    continue
                    
                sum_ = nums[std]+nums[left]+nums[right]
                
                cur_diff = abs(sum_-target)
                if cur_diff < dis:
                    dis = cur_diff
                    result = sum_    
                    
                if sum_ == target:
                    return sum_
                

                    
                if sum_ > target:
                    right -= 1
                elif sum_ < target:
                    left += 1
                    
        return result