class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        piles[i] - number of bananas in pile
        h = hours you have to eat all

        decide k = bananas per hour rate
        """
       
        minimum = 1
        maximum = max(piles)
        res = maximum
        
        while maximum >= minimum:
            k = (minimum + maximum) //2
            count = 0
            for val in piles:
                count += math.ceil(float(val) / k)
            if count > h:
                minimum = k+1
            else:
                res = k
                maximum = k-1
        return res