# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) > len(set(nums)):
            return True
        else:
            return False