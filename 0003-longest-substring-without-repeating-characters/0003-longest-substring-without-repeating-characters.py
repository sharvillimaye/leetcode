class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left, right = 0, 1
        max_length = 1
        length = 1
        letters = set(s[left])

        while right < len(s):
            if s[right] not in letters:
                length += 1
                letters.add(s[right])
                max_length = max(max_length, length)
            else:
                left = right
                length = 1
                letters = set(s[left])
            right += 1
        
        return max_length


