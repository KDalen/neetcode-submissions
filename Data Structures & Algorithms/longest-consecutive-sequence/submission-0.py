class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_len = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in numbers:
                current_len = 1
                counter = 1
                while nums[i] + counter in numbers:
                    counter +=1
                    current_len+=1
                if current_len > max_len:
                    max_len = current_len
        return max_len
                
