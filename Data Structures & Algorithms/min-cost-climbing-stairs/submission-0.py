class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # topdown memoisation
        # bottom up tabulation
        # bottom up no memory
        memo = {0:cost[0], 1:cost[1]}

        def dfs(i):
            if i in memo:
                return memo[i]
            memo[i] = min(cost[i] +dfs(i-1), cost[i] + dfs(i-2))

            return memo[i]
        return min(dfs(len(cost)-1),dfs(len(cost)-2))