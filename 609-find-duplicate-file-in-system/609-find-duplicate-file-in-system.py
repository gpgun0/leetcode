class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        map_ = {}
        
        for path in paths:
            pathAndFiles = path.split()
            path = pathAndFiles[0]
            
            for file in pathAndFiles[1:]:
                fileName, content = file.split("(")
                if not content in map_:
                    map_[content] = []
                    
                map_[content].append(path + "/" + fileName)
        
        result = []
        for k in map_:
            if len(map_[k]) > 1:
                result.append(map_[k])
            
        return result