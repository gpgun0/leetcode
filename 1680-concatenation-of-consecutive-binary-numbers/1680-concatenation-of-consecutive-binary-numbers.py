import math

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        prev = 1
        
        for i in range(2, n+1):
            prev <<= math.floor(math.log2(i))+1
            prev += i
            prev %= 10**9 + 7
            
        return prev%(10**9 + 7)