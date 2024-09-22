class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        minimum_rate = high

        while low <= high:
            middle = low + ((high - low) // 2)

            hours = 0
            for pile in piles:
                hours += int(pile / middle) + (pile % middle > 0)
            
            if hours > h:
                low = middle + 1
            else:
                minimum_rate = min(minimum_rate, middle)
                high = middle - 1
        
        return minimum_rate