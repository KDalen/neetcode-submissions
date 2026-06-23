class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        res = [] 
    
        def backtrack(openN,closedN):
            if openN == n and closedN == n:
                res.append("".join(path))
                return
            
            if openN < n:
                path.append("(")
                backtrack(openN+1,closedN)
                path.pop()
            if openN > closedN:
                path.append(")")
                backtrack(openN,closedN+1)
                path.pop()
        backtrack(0,0)
        return res