class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        import array
        
        len_of_nums = len(nums)

        ans_array = array.array('i', [])

        for i in range(0, len_of_nums):
            ans_array.insert(i, nums[i])
            ans_array.insert(i+len_of_nums, nums[i])
        
        return list(ans_array)


        for i in range(0, len_of_nums):
            nums.append(nums[i])

        return nums

        