class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict
        sorted_chars_wise_strs = defaultdict(list)

        for strr in strs:
            key = "".join(sorted(list(strr)))
            sorted_chars_wise_strs [key].append(strr)
        
        return list(sorted_chars_wise_strs.values())