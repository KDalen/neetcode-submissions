class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = []
        p = [False] *len(nums)
        res = []
        def dfs(perm, nums, pick):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    pick[i] = True
                    perm.append(nums[i])
                    dfs(perm, nums, pick)
                    perm.pop()
                    pick[i] = False
        dfs(perm, nums, p)
        return res
                
                
