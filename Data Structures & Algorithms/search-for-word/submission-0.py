class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def backtrack(r,c,i):
            if i == len(word):
                return True

            if r < 0 or c<0 or c>=COLS or r >= ROWS or word[i] != board[r][c] or board[r][c] == "#":
                return False

            board[r][c] = "#"

            res = (
                backtrack(r+1,c,i+1) or
                backtrack(r,c+1,i+1) or
                backtrack(r-1,c,i+1) or
                backtrack(r,c-1,i+1) 
            )
            #restores letter
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                out = backtrack(r,c,0)
                if out:
                    return out
        return False
