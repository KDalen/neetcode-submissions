# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            curr, low, high = stack.pop()
            
            if not curr:
                continue

            if not curr.val > low or  not curr.val < high:
                return False

            stack.append([curr.left,low, min(high, curr.val)])
            stack.append([curr.right, max(low, curr.val), high])
        return True