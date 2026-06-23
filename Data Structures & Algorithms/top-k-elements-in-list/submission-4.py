class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for val in nums:
            res[val] +=1

        res = sorted(res.items(), key= lambda item: item[1], reverse=True)

        return [r[0] for r in res[:k]]