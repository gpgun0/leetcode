class Solution:
    def isHappy(self, n: int) -> bool:
        hash_map = defaultdict(int)

        while n != 1:
            if hash_map[n]:
                return False
                
            hash_map[n] += 1

            temp = 0

            for str_num in str(n):
                temp += int(str_num)**2
            
            n = temp
        
        return True