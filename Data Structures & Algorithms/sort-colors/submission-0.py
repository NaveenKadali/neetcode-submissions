class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        color_frequencies = [0]*3
        for color in nums:
            color_frequencies[color] += 1
        
        index = 0
        for color, frequency in enumerate(color_frequencies):
            for _ in range(frequency):
                nums[index] = color
                index += 1