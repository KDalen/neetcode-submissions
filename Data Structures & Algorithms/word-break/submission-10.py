class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in res:
                return res[i]
            for j in range(len(wordDict)):
                n = len(wordDict[j])
                if s[i:i+n] == wordDict[j] and dfs(i+n):
                    res[i] = True
                    return res[i]
            res[i] = False
            return res[i]
        return dfs(0)
                    
