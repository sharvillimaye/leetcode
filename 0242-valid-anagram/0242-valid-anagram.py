class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency_s = {}
        frequency_t = {}
        for index in range(len(s)):
            frequency_s[s[index]] = frequency_s.get(s[index], 0) + 1
            frequency_t[t[index]] = frequency_t.get(t[index], 0) + 1        
        
        return frequency_s == frequency_t