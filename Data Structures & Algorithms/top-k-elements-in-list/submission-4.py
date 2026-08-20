class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if k == len(nums):
            return nums
        
        num_frequency_counter = defaultdict(int)
        for num in nums:
            num_frequency_counter[num] += 1

        highest_frequency = max(num_frequency_counter.values())
        num_frequency_buckets = [[] for i in range(1, highest_frequency + 1)]

        for key, value in num_frequency_counter.items():
            num_frequency_buckets[value-1].append(key)
        

        top_k_frequent_numbers = []
        for frequency in range(highest_frequency, 0, -1):
            bucket = num_frequency_buckets[frequency-1]
            
            for num in bucket:
                top_k_frequent_numbers.append(num)
                k-=1
            
            if not k>0:
                break
        
        return top_k_frequent_numbers
            