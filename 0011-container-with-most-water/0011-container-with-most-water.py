class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maximum_capacity = 0
        while left < right:
            current_capacity = min(height[left], height[right]) * (right - left)
            maximum_capacity = max(maximum_capacity, current_capacity)

            if height[left] <= height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
        
        return maximum_capacity
        