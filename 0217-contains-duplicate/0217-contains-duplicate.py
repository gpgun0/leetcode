class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        if any(val > 1 for key, val in counter.items()):
            return True

        return False