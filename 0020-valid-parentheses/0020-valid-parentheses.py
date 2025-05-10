class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == "(":
                stack.append("(")

            elif char == ")":
                if not len(stack) or stack[-1] != "(":
                    return False
                stack.pop()
            
            elif char == "{":
                stack.append("{")
            
            elif char == "}":
                if not len(stack) or stack[-1] != "{":
                    return False
                stack.pop()
            
            elif char == "[":
                stack.append("[")
            
            else:
                if not len(stack) or stack[-1] != "[":
                    return False
                stack.pop()

        if len(stack):
            return False

        return True
            