class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        
        if all(map(lambda x: x=='a', palindrome)):
            return palindrome[:-1] + "b"
        
        if all(map(lambda x: x=='a', palindrome[:len(palindrome)//2])) and\
            all(map(lambda x: x=='a', palindrome[len(palindrome)//2+1:])) and\
            palindrome[len(palindrome)//2] != 'a':
            return palindrome[:-1] + "b"
        
        
        for i in range(len(palindrome)):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i+1:]