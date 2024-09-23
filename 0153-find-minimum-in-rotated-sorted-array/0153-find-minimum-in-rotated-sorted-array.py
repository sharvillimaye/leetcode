import math

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        result = math.inf

        while left <= right:
            middle = left + ((right - left) // 2)
            result = min(result, nums[middle])

            if nums[middle] < nums[right]:
                right = middle - 1
            else:
                if nums[middle] > nums[left]:
                    if nums[right] < nums[left]:
                        left = middle + 1
                    else:
                        right = middle - 1
                else:
                    left = middle + 1
        
        return result