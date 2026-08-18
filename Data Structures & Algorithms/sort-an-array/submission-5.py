class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        array_len = len(nums)
        
        conitnue_to_sort = True
        while conitnue_to_sort :
            
            swapping_occured = False

            for i in range(1, array_len):

                if nums[i-1]>nums[i]:
                    temp = nums[i]
                    nums[i] = nums[i-1]
                    nums[i-1] = temp
                    swap_occured = 1

                    swapping_occured = True
            
            if swapping_occured:
                conitnue_to_sort = True
            else:
                conitnue_to_sort = False
            
        
        return nums