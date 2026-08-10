from array import array
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        nums_array = array('i', nums)
        nums_found_so_far_array = set()

        for num in nums_array:
            if num in nums_found_so_far_array:
                return True
            else:
                nums_found_so_far_array.add(num)
        
        return False