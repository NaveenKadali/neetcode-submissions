class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        len_of_strings = len(s)
        count_diff_arr = [0] * 26



        for i in range(len(s)):

            value_of_char_in_s = ord(s[i])
            value_of_char_in_t = ord(t[i])

            count_diff_arr[value_of_char_in_s-97] += 1
            count_diff_arr[value_of_char_in_t-97] -= 1
        
        print(count_diff_arr)

        if count_diff_arr.count(0) == 26:
            return True
        else:
            return False

