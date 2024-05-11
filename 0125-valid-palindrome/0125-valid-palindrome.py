class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.isalnum(s[left]):
                left += 1
            while left < right and not self.isalnum(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True

    def isalnum(self, c):
        return "a" <= c <= "z" or "A" <= c <= "Z" or "0" <= c <= "9"