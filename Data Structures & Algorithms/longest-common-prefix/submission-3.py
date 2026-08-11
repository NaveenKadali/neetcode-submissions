class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common_prefix = ""

        strs= sorted(strs)

        first_str = strs[0]
        last_str = strs[-1]

        for i, char in enumerate(first_str):
            if last_str[i] == char:
                common_prefix += char
            else:
                break      

        return common_prefix