class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        letters_s1 = {}
        for letter in s1:
            letters_s1[letter] = 1 + letters_s1.get(letter, 0)
        
        left = 0
        for right in range(left + len(s1) - 1, len(s2)):
            letters_s2 = {}
            for index in range(left, right + 1):
                letters_s2[s2[index]] = 1 + letters_s2.get(s2[index], 0)
            if letters_s2 == letters_s1:
                return True
            left += 1
        
        return False