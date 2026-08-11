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
        
        for i in range(shortest_string_length, -1, -1):

            for j in range (no_of_strings_given):
                if strs[j].startswith(shortest_string[0:i]):
                    pass
                else:
                    break
            else:
                common_prefix = shortest_string[0: i]
                break


        return common_prefix