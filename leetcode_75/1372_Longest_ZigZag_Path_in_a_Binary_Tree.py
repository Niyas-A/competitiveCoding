# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.helper(root.left,True,0),self.helper(root.right,False,0))
        
    def helper(self, root, isLeft, depth):
        if not root:
            return depth
        if isLeft:
            depth = max(
                depth, 
                self.helper(root.right, False, depth + 1),
                self.helper(root.left, True, 0)
            )
        else:
            depth = max(
                depth, 
                self.helper(root.left, True, depth + 1),
                self.helper(root.right, False, 0)
            )
        return depth