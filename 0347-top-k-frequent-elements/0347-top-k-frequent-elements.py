class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for element in nums:
            hashmap[element] = 1 + hashmap.get(element, 0)
        
        sorted_hashmap = sorted(hashmap.items(), key=lambda x:x[1], reverse=True)
        result = []
        for element in sorted_hashmap:
            result.append(element[0])
            if len(result) == k:
                return result