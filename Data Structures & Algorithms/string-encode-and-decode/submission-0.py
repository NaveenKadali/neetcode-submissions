class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""

        for str_ in strs:
            encoded_string += str(len(str_)) + "#"
            encoded_string += str_

        return encoded_string

    def decode(self, s: str) -> List[str]:

        print(s)

        decoded_strings = []
        
        sub_str_len = ''        
        
        index = 0
        while index < len(s):

            char = s[index]

            if char.isdigit():
                sub_str_len += char

            elif char == '#':

                ss_len = int(sub_str_len)

                print(ss_len)
                
                print("Inner: ", char, sub_str_len, ss_len)

                stop_index = index + int(sub_str_len)
                ss = s[index+1: stop_index+1]
                decoded_strings.append(ss)

                sub_str_len = ""
                index = stop_index
            
            index += 1
        
        return decoded_strings
