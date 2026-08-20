class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if k == len(nums):
            return nums
        
        num_frequency_counter = [[0, i] for i in range(-1000, 10002)]

        for num in nums:
            num_frequency_counter[num+1000][0] += 1

        num_frequency_counter.sort(reverse=True)

        top_k_frequent_numbers = [num_frequency_counter[i][1] for i in range(k)]
        
        return top_k_frequent_numbers
            