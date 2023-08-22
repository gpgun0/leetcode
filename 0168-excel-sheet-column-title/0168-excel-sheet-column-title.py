class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber:
            num = columnNumber % 26

            if num == 0:
                result = "Z" + result
                columnNumber = (columnNumber-26) // 26
            
            else:
                result = chr(num+64) + result
                columnNumber = columnNumber // 26


        return result 