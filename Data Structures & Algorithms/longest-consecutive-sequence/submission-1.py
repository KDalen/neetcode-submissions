class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_len = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in numbers:
                
                counter = 1
                while nums[i] + counter in numbers:
                    counter +=1
                max_len = max(max_len, counter)
                
        return max_len
                
