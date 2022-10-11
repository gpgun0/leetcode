class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        stack = [nums[0]]
        
        for i in range(1, len(nums)):            
            if stack[-1] < nums[i]:
                stack.append(nums[i])
                
                if len(stack) >= 3:
                    return True
                
                continue
                
            for j in range(len(stack)):
                if stack[j] >= nums[i]:
                    stack[j] = nums[i]
                    break
        
        return False
