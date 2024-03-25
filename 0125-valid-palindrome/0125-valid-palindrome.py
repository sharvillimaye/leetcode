class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for element in s:
            if element.isalnum():
                string += element.lower()
        reversed_string = string[::-1]
        return string == reversed_string