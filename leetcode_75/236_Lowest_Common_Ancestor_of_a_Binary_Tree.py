# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root == p or root == q:
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        else:
            return l or r

    #     self.found = [0 ,0]
    #     self.helper(root, p, q)
    #     return p
    
    # def helper(self, root, p, q):
    #     if root is None:
    #         return
    #     if root == p:
    #         print('p found')
    #         self.found[0] = 1
    #     if root == q:
    #         print('q found')
    #         self.found[1] = 1
    #     self.helper(root.left, p, q)
    #     self.helper(root.right, p, q) 
    #     if self.found[0] == 1 and self.found[1] == 1:
    #         print('node: ', root)
    #     return