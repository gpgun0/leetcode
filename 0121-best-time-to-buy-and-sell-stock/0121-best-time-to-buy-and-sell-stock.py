class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        min_price = prices[0]

        for price in prices[1:]:

            answer = max(answer, price - min_price)
            
            min_price = min(min_price, price)
            


        return answer