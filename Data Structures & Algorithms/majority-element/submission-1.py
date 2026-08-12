class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        from collections import defaultdict
        num_wise_count = defaultdict(int)

        for num in nums:
            num_wise_count[num] += 1
        
        max_count = max(list(num_wise_count.values()))

        for num, count in num_wise_count.items():
            
            if count == max_count:
                return num
