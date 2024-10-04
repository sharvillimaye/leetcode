class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        product = 1
        for num in nums:
            product *= num
            left.append(product)
        
        right = [0] * len(nums)
        product = 1
        for index in range(len(nums)-1, -1, -1):
            product *= nums[index]
            right[index] = product

        print(left)
        print(right)
        
        result = []
        for index in range(len(nums)):
            left_number = 1
            if index - 1 >= 0:
                left_number = left[index - 1]

            right_number = 1
            if index + 1 < len(nums):
                right_number = right[index + 1]
            
            result.append(left_number * right_number)
        
        return result
