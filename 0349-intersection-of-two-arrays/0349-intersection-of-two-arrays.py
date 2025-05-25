class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = defaultdict(int)
        output = []

        for num in nums1:
            counter[num] += 1

        for num in nums2:
            if counter[num] and not num in output:
                output.append(num)
        
        return output