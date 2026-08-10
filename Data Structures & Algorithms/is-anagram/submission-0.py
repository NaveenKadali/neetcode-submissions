class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        """ Approach 1:

            compare the legnth of s and t, return false if differnt.

            form two arrays: one for storing the characters in s and another for    characters in t 
            sort both the arrays
            iterate from 0 to len(s or t) and compare the elements in the sorted arrays, if differnt return false
            return true at the last

            """
            # Approach 1:
        s_chars = []
        t_chars = []
        
        for char in s:
            s_chars.append(char)
        
        for char in t:
            t_chars.append(char)
        
        s_chars = sorted(s_chars)
        t_chars = sorted(t_chars)

        return True if s_chars == t_chars else False


        """ Approach 2:
            create 2 dicts to maintain character wise count
            iterate character by character by character over s
            create the dict, if the character already in dict then increase     value by one, if not available: assign the value as 1

            iterate over any one dict and check if key exists in another dict or not, if not: return False, if exists: check the count -> return false if count doesn't match -> countineu with next next key if count matches.
        """