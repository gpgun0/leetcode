class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        
        dic = defaultdict(list)
        
        for word in strs:
            dic[str(sorted(word))].append(word)
        
        for key, value in dic.items():
            result.append(value)
        
        return result