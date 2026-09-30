class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(val):
            if val == 0:
                return 0
            if val in memo:
                return memo[val]
            res = float("inf")
            for coin in coins:
                if val >= coin:
                    res = min(res, 1 + dfs(val - coin))
                    memo[val] = res
            return res
                
        minCoins = dfs(amount)
        return -1 if minCoins >= float("inf") else minCoins