# 27. Remove Element
# https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        write_index = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_index] = nums[i]
                write_index += 1

        for i in range(write_index, len(nums)):
            nums[i] = '_'
        
        return write_index