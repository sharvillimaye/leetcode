class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for element in s:
            if element == '(' or element == '[' or element == '{':
                stack.append(element)
            elif element == ')' or element == ']' or element == '}':
                if not stack:
                    return False
                beginning_bracket = stack.pop()
                match beginning_bracket:
                    case '(': 
                        if element != ')':
                            return False
                    case '[': 
                        if element != ']':
                            return False
                    case '{': 
                        if element != '}':
                            return False
        
        if stack:
            return False
        
        return True
        