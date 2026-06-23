class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        candidates.sort()
        def backtrack(idx, total):
            #base case
            if target == total:
                
                res.append(path.copy())
                return
            if total > target or len(candidates) <= idx:
                return
            
            #backtracking
            path.append(candidates[idx])
            backtrack(idx+1, total+candidates[idx])
            path.pop()


            # option 2
            while idx +1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx+=1
            backtrack(idx+1, total)

        backtrack(0,0)
        return res