class Solution:
    def climbStairs(self, n: int) -> int:
        #top down so reccursive

        memo = {}
        def topdown(i):
            if i == 0:
                return 1
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = topdown(i-1) + topdown(i-2)
            return memo[i]
        return topdown(n)