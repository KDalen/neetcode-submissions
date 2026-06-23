class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # topdown memoisation
        # bottom up tabulation -->
        # bottom up no memory 
        arr = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            new =  min(arr[i-1] + cost[i], arr[i-2] + cost[i])
            arr.append(new)
        return min(arr[-1], arr[-2])

        
