class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict
        
        character_frequency_counter_wise_strs = defaultdict(list)

        for i, word in enumerate(strs):
            
            charactier_frequency_counter = [0]*26
            for char in word:
                character_index = ord(char) - ord('a')
                charactier_frequency_counter [character_index] += 1
            
            character_frequency_counter_wise_strs[tuple(charactier_frequency_counter )].append(word)

        return list(character_frequency_counter_wise_strs.values())


                
        