class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {k:0 for k in set(nums)}
        for val in nums:
            res[val] += 1
        return heapq.nlargest(k, res.keys(), key=res.get)