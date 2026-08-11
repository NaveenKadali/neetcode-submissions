class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        nutralization_dict = dict()

        for i in range(len(s)):

            char_in_s = s[i]
            char_in_t = t[i]

            nutralization_dict[char_in_s] = 1 + nutralization_dict.get(char_in_s, 0)
            nutralization_dict[char_in_t] = nutralization_dict.get(char_in_t, 0) - 1

        if set(nutralization_dict.values()) == {0}:
            return True
        else:
            return False

