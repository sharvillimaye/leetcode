class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for element in strs:
            sorted_element = "".join(sorted(element))
            if sorted_element in hashmap:
                hashmap[sorted_element].append(element)
            else:
                hashmap[sorted_element] = [element]
        
        result = []
        for key, array in hashmap.items():
            result.append(array)
        return result