class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer < right_pointer:
            while not self.alphanum(s[left_pointer]) and left_pointer < len(s) - 1:
                left_pointer += 1
            while not self.alphanum(s[right_pointer]) and right_pointer >= 0:
                right_pointer -= 1
            
            if s[left_pointer].lower() != s[right_pointer].lower():
                return False
            
            left_pointer += 1
            right_pointer -= 1
            
        return True
    
    def alphanum(self, c):
        return ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9')
