class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        num_frequency_counter = [0]*100001

        for num in nums:
            num_frequency_counter[num+50000] += 1
        
        nums.clear()
        for index, frequency in enumerate(num_frequency_counter):
            for i in range(frequency):
                nums.append(index-50000)
        
        return nums