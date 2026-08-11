class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common_prefix = ""

        shortest_string = strs[0]
        shortest_string_length = len(shortest_string)
        no_of_strings_given = len(strs)

        for string in strs:

            if string == "":
                return common_prefix

            if len(string) < shortest_string_length:
                shortest_string = string
                shortest_string_length = len(shortest_string)
        
        no_more_common_prefix = False
        for i in range(0, shortest_string_length):

            for strr in strs:
                if shortest_string[i] == strr[i]:
                    pass
                else:
                    no_more_common_prefix = True
                    break
            else:
                common_prefix += shortest_string[i]
            
            if no_more_common_prefix:
                break

        return common_prefix