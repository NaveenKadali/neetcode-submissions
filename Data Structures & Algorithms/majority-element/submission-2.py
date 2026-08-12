class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        majority_element = nums[n//2]

        return majority_element

