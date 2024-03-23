class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        longest = 0

        for value in values:
            if value - 1 not in values:
                length = 0
                while (value + length) in values:
                    length += 1
                longest = max(length, longest)
        
        return longest