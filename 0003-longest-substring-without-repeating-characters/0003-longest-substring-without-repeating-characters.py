class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        left = 0
        result = 0
        letters = set()

        for right in range(len(s)):
            while s[right] in letters:
                letters.remove(s[left])
                left += 1
            letters.add(s[right])
            result = max(result, right - left + 1)

        return result