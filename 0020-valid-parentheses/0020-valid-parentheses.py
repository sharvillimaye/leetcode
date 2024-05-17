class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {')':'(', '}':'{', ']':'['}

        for element in s:
            if element not in dictionary:
                stack.append(element)
                continue
            if not stack or stack[-1] != dictionary[element]:
                return False
            stack.pop()
            
        return not stack