class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}
        for string in strs:
            if tuple(sorted(string)) in hashtable:
                # add to old group
                hashtable[tuple(sorted(string))].append(string)
            else:
                # create a new group
                hashtable[tuple(sorted(string))] = [string]

        result = []
        for key in hashtable:
            result.append(hashtable[key])
        return result