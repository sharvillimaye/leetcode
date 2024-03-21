class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = [1] * len(nums)

        prefix = 1
        for index in range(len(nums)):
            solution[index] = prefix
            prefix *= nums[index]
        
        suffix = 1
        for index in range(len(nums) - 1, -1, -1):
            solution[index] *= suffix
            suffix *= nums[index]
        
        return solution