class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for element in nums:
            count[element] = 1 + count.get(element, 0)
        for number, count in count.items():
            freq[count].append(number)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for number in freq[i]:
                result.append(number)
                if len(result) == k:
                    return result
        
        sorted_hashmap = sorted(hashmap.items(), key=lambda x:x[1], reverse=True)
        result = []
        for element in sorted_hashmap:
            result.append(element[0])
            if len(result) == k:
                return result