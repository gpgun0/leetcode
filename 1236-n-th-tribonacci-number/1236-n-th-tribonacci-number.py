class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1
        
        t0, t1, t2 = 0, 1, 1
        
        for i in range(n-2):
            
            t0, t1, t2 = t1, t2, t0+t1+t2
                 
        return t2