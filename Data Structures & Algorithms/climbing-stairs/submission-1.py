class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(i):
            if i <= 1:
                return 1
            if i not in memo:
                memo[i] = helper(i-1) + helper(i-2)  
            print(memo[i])
            return memo[i]  
        return helper(n) 