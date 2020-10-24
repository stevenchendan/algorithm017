# https://leetcode.com/problems/group-anagrams/
# solution 1: sorted item in strs list and then use hash table to store the items
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in strs:
            temp = "".join(sorted(list(i)))
            if temp in dict.keys():
                dict[temp].append(i)
            else:
                dict[temp] = [i]
        return list(dict.values())
        
        
        