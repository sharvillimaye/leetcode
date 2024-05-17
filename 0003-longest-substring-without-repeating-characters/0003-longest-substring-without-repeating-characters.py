class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        left, right = 0, 0
        length = 0
        letters = set()

        while right < len(s):
            while s[right] in letters:
                letters.remove(s[left])
                left += 1
            
            length = max(length, right - left + 1)
            letters.add(s[right])
            right += 1
        
        return length
        