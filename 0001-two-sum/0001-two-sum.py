class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, element in enumerate(nums):
            num_needed = target - nums[index]
            if num_needed in hashmap:
                return [index, hashmap[num_needed]]
            hashmap[element] = index
