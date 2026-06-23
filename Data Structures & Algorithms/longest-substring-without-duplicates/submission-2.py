class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charMap:
                charMap.remove(s[l])
                l+=1
            charMap.add(s[r])
            res = max(r-l+1, res)
        return res