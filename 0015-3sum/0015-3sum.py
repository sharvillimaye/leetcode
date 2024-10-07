class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        for index, element in enumerate(nums):
            if element > 0:
                break
            
            if index > 0 and element == nums[index - 1]:
                continue
            
            left, right = index + 1, len(nums) - 1
            while left < right:
                current = element + nums[left] + nums[right]
                if current > 0:
                    right -= 1
                elif current < 0:
                    left += 1
                else:
                    result.append([element, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result