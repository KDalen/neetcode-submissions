class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        memo = {}
        for i in range(len(s)):
            if s[i] in memo:
                memo[s[i]] += 1
            else:
                memo[s[i]] = 1
        print(memo)
        for char in t:
            if char in memo:
                memo[char] -=1
                
                if memo[char] == 0:
                    del memo[char]
            else:
                return False
        return len(memo) == 0