class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {}
        def dp(i, end):
            if i >= end:
                return 0
            if (i, end) in memo:
                return memo[(i, end)]
            memo[(i,end)]= max(dp(i+1, end), dp(i+2, end)+ nums[i])
            return memo[(i,end)]
        return max(dp(0,len(nums)-1), dp(1, len(nums)))