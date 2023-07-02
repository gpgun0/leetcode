from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counter = Counter(nums)
        q = []

        for num, freq in counter.items():
            heappush(q, (-freq, num))
        
        for _ in range(k):
            num = heappop(q)[1]
            result.append(num)

        return result
