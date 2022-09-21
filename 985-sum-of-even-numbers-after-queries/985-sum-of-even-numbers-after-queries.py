class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_ = 0
        for num in nums:
            if num%2 == 0:
                sum_ += num
        
        answer = []
        for query in queries:
            prev_ = nums[query[1]]
            next_ = nums[query[1]] + query[0]
            
            if next_%2 == 1:
                if prev_%2 == 0:
                    sum_ -= prev_
            
            elif next_%2 == 0:
                if query[0]%2 == 1:
                    sum_ += (prev_ + query[0])
                elif query[0]%2 == 0:
                    sum_ += query[0]
            answer.append(sum_)
            
            nums[query[1]] = next_
        
        return answer