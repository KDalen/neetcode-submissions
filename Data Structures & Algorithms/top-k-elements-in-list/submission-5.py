class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)

        for i in range(len(nums)):
            frequencies[nums[i]] += 1

        buckets = [[] for i in range(len(nums) +1)]
        print(buckets)
        for num, cnt in frequencies.items():
            buckets[cnt].append(num)
        
        res = []

        for i in range(len(buckets) -1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res)==k:
                    return res

        
