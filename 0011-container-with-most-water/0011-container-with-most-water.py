class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        result = 0

        while l < r:
            current_water = (r - l) * min(height[r], height[l])
            result = max(result, current_water)

            if height[l] <= height[r] and l < r:
                l += 1
            elif height[l] > height[r] and l < r:
                r -= 1
            else:
                print(l, r)
                return result
        
        return result
            



        