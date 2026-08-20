class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if k == len(nums):
            return nums
        
        num_frequency_counter = [0]*2001

        for num in nums:
            num_frequency_counter[num+1000] += 1

        top_k_frequent_numbers = []
        while k>0:

            max_frequency = max(num_frequency_counter)
            for index, frequency in enumerate(num_frequency_counter):

                if frequency == max_frequency:
                    top_k_frequent_numbers.append(index-1000)
                    num_frequency_counter[index] &= 0
                    k-=1
                
                if not k>0:
                    break
        
        return top_k_frequent_numbers
            