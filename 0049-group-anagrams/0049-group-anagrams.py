class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            hash_map[sorted_s].append(s)
        
        return list(hash_map.values())

