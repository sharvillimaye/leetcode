class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0
        
        for num in nums:    
            if num - 1 not in nums:
                current = num
                length = 0
                while current in nums:
                    current += 1
                    length += 1
                result = max(result, length)
        
        return result
