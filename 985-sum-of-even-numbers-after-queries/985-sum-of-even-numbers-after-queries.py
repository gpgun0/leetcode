class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_ = 0
        for num in nums:
            if num%2 == 0:
                sum_ += num
        
        
        answer = []
        for query in queries:
            
            if (nums[query[1]] + query[0])%2 == 1:
                if nums[query[1]]%2 == 0:
                    sum_ -= nums[query[1]]
            
            elif (nums[query[1]] + query[0])%2 == 0:
                if query[0]%2 == 1:
                    sum_ += (nums[query[1]] + query[0])
                elif query[0]%2 == 0:
                    sum_ += query[0]
            answer.append(sum_)
            
            nums[query[1]] = nums[query[1]] + query[0]
        
        return answer