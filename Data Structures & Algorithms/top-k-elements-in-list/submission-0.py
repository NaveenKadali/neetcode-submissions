class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import defaultdict

        frequency_of_nums = defaultdict(int)

        for num in nums:
            frequency_of_nums[num] += 1
        
        top_k_frequent_elements = []

        while k>0:

            max_frequency = max(frequency_of_nums.values())

            for key, value in frequency_of_nums.items():

                if value == max_frequency:
                    top_k_frequent_elements.append(key)
                    frequency_of_nums[key] = 0
                    k-=1
                
                if k<1:
                    break
            
        return top_k_frequent_elements