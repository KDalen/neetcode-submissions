class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        res = ""
        for j in range(len(s)):
            for i in range(2):
                l, r = j, j+i
                cur = ""
                while l >=0 and r < len(s) and s[l] == s[r]:
                    if l == r:
                        cur = s[l]
                    else:
                        cur = s[l]+cur+s[r]
                    if len(cur) > maxLen:
                        maxLen = len(cur)
                        res = cur
                    l-=1
                    r+=1

        return res