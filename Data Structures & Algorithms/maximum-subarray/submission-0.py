class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum =0 
        best = float("-inf")
        for i in range(len(nums)):
            
            if running_sum+nums[i] >= nums[i]:
                running_sum+= nums[i]
            else:
                running_sum = nums[i]
            best = max(best, running_sum)
        return best
