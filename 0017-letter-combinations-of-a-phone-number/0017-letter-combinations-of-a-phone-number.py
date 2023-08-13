class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if digits == "":
            return result

        n = len(digits)
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(i, letter):
            if i == n:
                result.append(letter)
                return

            for char in dic[ digits[i] ]:
                dfs(i+1, letter + char)
        
        dfs(0, "")
        return result