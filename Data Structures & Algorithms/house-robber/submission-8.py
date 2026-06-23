class Solution:
    def rob(self, nums: List[int]) -> int:
        dictionary = {}

        def helper(i):  
            if i> len(nums)-1:
                return 0
            if not i in dictionary:
                dictionary[i] = max(nums[i]+helper(i+2), helper(i+1))
            return dictionary[i]

        return helper(0)
