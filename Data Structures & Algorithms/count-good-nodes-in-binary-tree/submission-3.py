# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(r, maximum):

            if not r:
                return None
            if r.val >= maximum:
                self.res = self.res + 1
      
            maximum = max(r.val, maximum)
            
            dfs(r.left, maximum)
            dfs(r.right, maximum)

        dfs(root, float('-inf'))
        return self.res