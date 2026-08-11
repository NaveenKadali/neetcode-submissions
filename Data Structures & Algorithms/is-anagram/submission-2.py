class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Approach 2

        char_wise_count_for_s = dict()
        char_wise_count_for_t = dict()

        if len(s) != len(t):
            return False


        for char in s:
            if char in char_wise_count_for_s.keys():
                char_wise_count_for_s[char] = char_wise_count_for_s[char]+1
            else:
                char_wise_count_for_s[char] = 1
        
        for char in t:
            if char in char_wise_count_for_t.keys():
                char_wise_count_for_t[char] = char_wise_count_for_t[char]+1
            else:
                char_wise_count_for_t[char] = 1
        
        for key, value in char_wise_count_for_s.items():
            if key not in char_wise_count_for_t.keys():
                return False
            else:
                if char_wise_count_for_t[key] == value:
                    pass
                else:
                    return False
        
        return True      
        
        
        