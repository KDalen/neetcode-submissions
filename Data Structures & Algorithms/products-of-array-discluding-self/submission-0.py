class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
                if i!=j:
                    total*= nums[j]

            out.append(total)
        return out
