class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = Counter(list(stones))

        result = sum(map(lambda jewel: counter[jewel], jewels))
        
        return result