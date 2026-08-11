
class Solution:
    def twoSum(self, nums, target: int) -> List[int]:
        
        seen_element_indices = dict()
        for i in range(0, len(nums)):
            
            num = nums[i]
            required_compliment_value = target - num

            if required_compliment_value in seen_element_indices.keys():
                return [seen_element_indices[required_compliment_value], i]
            
            seen_element_indices[num] = i