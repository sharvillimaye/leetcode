class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        letters = {}
        for letter in s:
            if (letter not in letters):
                letters[letter] = 1
            else:
                letters[letter] += 1
        
        for letter in t:
            if (letter not in letters):
                return False
            
            letters[letter] -= 1
            if (letters[letter] < 0):
                return False
        
        return True