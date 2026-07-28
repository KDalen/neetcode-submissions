class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, r = 1, piles[-1]
        while l < r:
            mid = (l+r) // 2
       
            hours = 0
            for val in piles:
                hours += -(val // -mid)
            if hours > h:
                l = mid +1
            else:
                r=mid
        return l

