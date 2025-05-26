class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for string in strings:
            
            diff = ord(string[0]) - ord('a')
            
            key_string = ""

            for char in string:
                if ord(char) - diff < 97:
                    key_string += chr(ord(char) - diff + 26)
                else:
                    key_string += chr(ord(char) - diff)
                
            hash_map[key_string].append(string)
        
        return list(hash_map.values())