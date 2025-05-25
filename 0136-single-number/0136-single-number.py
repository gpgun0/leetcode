class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        for key, val in counter.items():
            if val == 1:
                return key