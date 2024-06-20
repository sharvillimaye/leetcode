class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        letter_map, reference_map = {}, {}
        min_result = ""

        for letter in t:
            reference_map[letter] = 1 + reference_map.get(letter, 0)
    
        for right in range(len(s)):
            letter_map[s[right]] = 1 + letter_map.get(s[right], 0)
            while (left <= right and self.checkMaps(reference_map, letter_map)):
                result = s[left:right+1]
                if (min_result == "" or right - left + 1 < len(min_result)):
                    min_result = s[left:right+1]
                letter_map[s[left]] -= 1
                left += 1
        return min_result
            
    def checkMaps(self, reference: map, letter: map) -> bool:
        for key, value in reference.items():
            if letter.get(key, 0) < value:
                return False
        return True