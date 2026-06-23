class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        starters = []
        for val in nums:
            if val - 1 not in numbers:
                starters.append(val)
        maxLen = 0
        for val in starters:
            curr = val
            while curr + 1 in numbers:
                curr += 1
            maxLen = max(maxLen, curr-val+1)
    
        return maxLen