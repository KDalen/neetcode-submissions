class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        for val in nums:
            if val in hashmap:
                return True
            hashmap.add(val)

        return False
