# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(r, depth):
            if not r:
                return None
            if depth == len(res):
                res.append(r.val)

            #check right then left
            dfs(r.right, depth+1)
            dfs(r.left, depth+1)
            
        dfs(root, 0)
        return res