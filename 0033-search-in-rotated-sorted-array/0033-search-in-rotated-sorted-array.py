class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)

        left = 0
        right = l-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] <= nums[-1]:
                right = mid - 1
            else:
                left = mid + 1
        
        # left -> 가장 작은 값

        def binary_search(left, right, target):

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left += 1
                else:
                    right -= 1
            
            return -1
        
        result = binary_search(0, left - 1, target)

        if result != -1:
            return result

        return binary_search(left, l - 1, target)



