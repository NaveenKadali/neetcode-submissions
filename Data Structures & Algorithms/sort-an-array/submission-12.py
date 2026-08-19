class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        
        array_len = len(nums)
        
        conitnue_to_sort = True
        while conitnue_to_sort:
            
            swap_occured = False

            for i in range(1, array_len):
                j = array_len - 2

                if nums[i - 1] > nums[i]:
                    temp = nums[i]
                    nums[i] = nums[i - 1]
                    nums[i - 1] = temp

                    swap_occured = True
                
                if nums[j] > nums[j + 1]:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp

                    swap_occured = True
            
            if swap_occured:
                conitnue_to_sort = True
            else:
                conitnue_to_sort = False
            
        return nums

"""
class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        
        array_len = len(nums)
        
        i = 1
        j = array_len-2

        if array_len <= 2:
            nums[0], nums[-1] = nums[-1], nums[0]
            return nums


        conitnue_to_sort = True

        while conitnue_to_sort :
            
            swap_occured = False
            if nums[i-1]>nums[i]:
                temp = nums[i]
                nums[i] = nums[i-1]
                nums[i-1] = temp

                swap_occured = True
            
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

                swap_occured = True
            
            if not swap_occured:
                i+= 1
                j-=1

                if i>=array_len and j<=0:
                    i = 1
                    j = array_len-2
                    break
        
        return nums

"""