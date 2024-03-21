class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = defaultdict(list)
        for string in strs:
            hashtable[tuple(sorted(string))].append(string)
        return hashtable.values()