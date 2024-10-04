class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for element in s:
            if element == "(" or element == "{" or element == "[":
                stack.append(element)
            else:
                if len(stack) > 0:
                    pair = stack.pop()
                    if element == ")" and pair != "(":
                        return False
                    elif element == "]" and pair != "[":
                        return False
                    elif element == "}" and pair != "{":
                        return False
                else:
                    return False
            
        return len(stack) == 0