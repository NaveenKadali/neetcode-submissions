class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        array_len = len(nums)

        for i in range(array_len):
            for j in range(i+1, array_len):
                
                if nums[i] > nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        
        return nums