class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        freq =[[] for _ in range(len(nums)+1)]
        for val in nums:
            res[val] = 1 + res.get(val, 0)
        for num, cnt in res.items():
            freq[cnt].append(num)

        ret = []
        for i in range(len(freq)-1,0, -1):
            for num in freq[i]:
                ret.append(num)
                if len(ret) == k:
                    return ret
