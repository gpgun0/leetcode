class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        dp = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        
        nums1 = [0] + nums1
        nums2=  [0] + nums2
        
        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
        
        max_ = 0
        for x in dp:
            max_ = max(max_, max(x))
        
        return max_