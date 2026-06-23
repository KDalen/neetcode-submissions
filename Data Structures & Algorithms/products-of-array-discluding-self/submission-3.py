class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix post fix
        pre = []
        product = 1
        for i in range(len(nums)):
            pre.append(product)
            product *= nums[i]
        
        post = []
        product = 1
        for i in range(len(nums)-1,-1,-1):

            post.append(product)
            product *= nums[i]
        print(pre,post)
        res = []
        for i in range(len(nums)):
            res.append(post[len(nums) - i-1]*pre[i])
        return res