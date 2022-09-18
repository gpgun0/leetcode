class Solution:
    def trap(self, height: List[int]) -> int:
        max_ = -1
        idx = 0
        
        for i in range(len(height)):
            if height[i] > max_:
                max_ = height[i]
                idx = i
        
        result = 0
        std = -1
        for i in range(idx):
            if std == -1:
                std = height[i]
            
            elif std >= height[i]:
                result += std-height[i]
            elif std < height[i]:
                std = height[i]
        
        std = -1
        for i in range(len(height)-1, idx, -1):    
            
            if std == -1:
                std = height[i]
            
            elif std >= height[i]:
                result += std-height[i]
            elif std < height[i]:
                std = height[i]
                
        return result