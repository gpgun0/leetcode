class Solution:
    def trap(self, height: List[int]) -> int:
        max_ = -1
        idx = 0
        
        for i in range(len(height)):
            if height[i] > max_:
                max_ = height[i]
                idx = i
        
        result = 0
        stack = []
        for i in range(idx):
            if not stack:
                stack.append(height[i])
            
            elif stack[-1] >= height[i]:
                result += stack[-1]-height[i]
            elif stack[-1] < height[i]:
                stack.append(height[i])
        
        stack = []
        for i in range(len(height)-1, idx, -1):    
            if not stack:
                stack.append(height[i])
            
            elif stack[-1] >= height[i]:
                result += stack[-1]-height[i]
            elif stack[-1] < height[i]:
                stack.append(height[i])
        
        return result