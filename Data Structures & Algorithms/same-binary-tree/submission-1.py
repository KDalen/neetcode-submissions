# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [[p,q]]

        while stack:
            l,r = stack.pop()
            if not (l or r):
                continue
            if l is None or r is None or l.val != r.val:
                return False
        
            stack.append([l.left, r.left])
            stack.append([l.right, r.right])

        return True
        