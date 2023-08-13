class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if digits == "":
            return result

        n = len(digits)
        dic = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }

        def dfs(i, letter):
            digit = digits[i]

            for char in dic[digit]:
                if i == n - 1:
                    result.append(letter + char)

                else:
                    dfs(i+1, letter + char)
        
        dfs(0, "")
        return result