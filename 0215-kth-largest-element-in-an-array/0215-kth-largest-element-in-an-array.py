class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxValue = max(nums)
        minValue = min(nums)

        count = [0]*(maxValue-minValue+1)

        for num in nums:
            count[num-minValue] += 1
        
        for i in range(len(count)-1, -1, -1):
            while count[i]:
                k -= 1
                count[i] -= 1

            if k < 1:
                return i + minValue
            
