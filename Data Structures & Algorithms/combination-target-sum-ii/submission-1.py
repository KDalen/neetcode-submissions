class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        candidates.sort()
        def backtrack(idx, total):
            #base case
            if target == total:
                if not path in res:
                    res.append(path.copy())
                return
            if total > target or len(candidates) <= idx:
                return

            #backtracking
            path.append(candidates[idx])
            backtrack(idx+1, total+candidates[idx])
            path.pop()
            backtrack(idx+1, total)

        backtrack(0,0)
        return res