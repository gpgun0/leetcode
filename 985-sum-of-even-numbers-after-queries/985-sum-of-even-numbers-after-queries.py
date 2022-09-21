class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_ = sum(x for x in nums if x%2 == 0)
        
        answer = []
        for val, idx in queries:
            if nums[idx]%2 == 0:
                sum_ -= nums[idx]
            nums[idx] += val
            if nums[idx]%2 == 0:
                sum_ += nums[idx]
        
            answer.append(sum_)

        return answer