from collections import deque

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        
        q = deque([changed[0]])
        result = []
        
        for i in range(1, len(changed)):
            if not q:
                q.append(changed[i])
                continue
                
            if q[0]*2 != changed[i]:
                q.append(changed[i])
            elif q[0]*2 == changed[i]:
                result.append(q.popleft())
        
        if q:
            return []
        return result