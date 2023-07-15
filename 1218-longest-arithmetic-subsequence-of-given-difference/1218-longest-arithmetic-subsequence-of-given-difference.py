class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        table = defaultdict(int)
        result = 1

        for num in arr:
            diff_num = num - difference

            if not table[diff_num]:
                table[num] = 1
            
            else:
                table[num] = table[diff_num] + 1
                result = max(result, table[num])
        
        return result