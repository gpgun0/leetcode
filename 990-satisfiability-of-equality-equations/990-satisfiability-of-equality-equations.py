class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]

        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return parent[x]
        
        def union(a, b):
            a = find(a)
            b = find(b)
            parent[max(a, b)] = min(a, b)
        
        equations.sort(key=lambda x: x[1], reverse=True)
        for equation in equations:
            first = ord(equation[0])-97
            second = ord(equation[3])-97
            if equation[1] == '=':
                union(first, second)
            
            elif equation[1] == '!':
                if find(first) == find(second):
                    return False
        
        return True