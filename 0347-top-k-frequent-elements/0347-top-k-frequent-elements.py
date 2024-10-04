class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        sorted_freq = sorted(freq.items(), key=lambda x:-x[1])
        result = []
        for element in sorted_freq:
            result.append(element[0])
            if len(result) == k:
                return result