class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        count_of_given_value = 0
        total_no_of_nums = 0

        for num in nums:

            if num == val:
                count_of_given_value += 1
            
            total_no_of_nums += 1

        k = total_no_of_nums-count_of_given_value

        for i in range(0, k):
            j = total_no_of_nums-1
            while nums[i] == val and i<k:

                if nums[j] != val:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
                
                j -= 1

        return k
