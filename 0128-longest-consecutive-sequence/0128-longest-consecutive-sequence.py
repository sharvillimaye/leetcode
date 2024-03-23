class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set()
        for element in nums:
            values.add(element)
        
        max_length = 0
        for value in values:
            if value - 1 in values:
                continue
            current_value = value
            current_length = 0
            while (current_value in values):
                current_length += 1
                current_value += 1
            if current_length > max_length:
                max_length = current_length
        
        return max_length