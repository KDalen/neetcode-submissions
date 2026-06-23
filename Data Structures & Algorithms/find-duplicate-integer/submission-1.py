class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for val in nums:
            if nums[abs(val)-1] < 0:
                return abs(val)
            else:
                nums[abs(val)-1] *= -1
        return -1