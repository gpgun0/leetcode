class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        answer = 0

        left, right = 0, n-1

        while left < right:
            height_left, height_right = height[left], height[right]
            w = right - left
            h = min(height_left, height_right)
            answer = max(answer, w*h)

            if height_left <= height_right:
                left += 1
            else:
                right -= 1
            
        return answer