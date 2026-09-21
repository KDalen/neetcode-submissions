"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        stack = [node]
        head =  Node(node.val)
        copies = {node: head}
        while stack:
            cur_node = stack.pop()
            for neighbor in cur_node.neighbors:
                if neighbor not in copies:
                    copies[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)

                copies[cur_node].neighbors.append(copies[neighbor])
                
        return head

