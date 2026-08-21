class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product_of_elements_from_left_to_right = []
        product_of_elements_from_right_to_left = []
            
        prefix = 1
        count_of_nums = len(nums)
        for i in range(count_of_nums):
            prefix = prefix * nums[i]
            product_of_elements_from_left_to_right.append(prefix)

        prefix = 1
        for i in range(count_of_nums-1, -1, -1):
            prefix = prefix * nums[i]
            product_of_elements_from_right_to_left.append(prefix)
        
        product_of_elements_from_right_to_left.reverse()

        result = []
        for i in range(count_of_nums):
            
            if i == 0:
                suffix_product = 1
                prefix_product = product_of_elements_from_right_to_left[i+1]

            elif i == count_of_nums-1:
                prefix_product = 1
                suffix_product = product_of_elements_from_left_to_right[i-1]

            else:
                suffix_product = product_of_elements_from_left_to_right[i-1]
                prefix_product = product_of_elements_from_right_to_left[i+1]
            
            result.append(suffix_product*prefix_product)

        return result



        

            

        