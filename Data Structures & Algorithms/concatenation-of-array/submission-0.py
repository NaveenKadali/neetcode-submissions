class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        len_of_nums = len(nums)
        for i in range(0, len_of_nums):
            nums.append(nums[i])

        return nums