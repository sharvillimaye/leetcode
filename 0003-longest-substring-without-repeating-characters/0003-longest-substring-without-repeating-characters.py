class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        left, right = 0, 0
        max_length = 0
        length = 0
        letters = set()

        while right < len(s):
            if s[right] not in letters:
                length += 1
                letters.add(s[right])
                max_length = max(max_length, length)
                right += 1
            else:
                letters.remove(s[left])
                left += 1
                length -= 1
                
        return max_length