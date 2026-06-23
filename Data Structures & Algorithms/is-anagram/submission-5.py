class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hs, ht = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            hs[s[i]] += 1
            ht[t[i]] += 1

        return ht == hs