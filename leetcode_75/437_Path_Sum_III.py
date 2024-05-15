# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """

        def dfs(root, ps):
            if root is None:
                return
            cs = ps + root.val
            x = cs - targetSum
            if x in freq:
                self.count += freq[x]
            if cs in freq:
                freq[cs] += 1
            else:
                freq[cs] = 1

            dfs(root.left, cs)
            dfs(root.right, cs)
            freq[cs] -= 1

        self.count = 0
        freq = {0:1}
        dfs(root, 0)
        return self.count

        # if targetSum == 0:
        #     return 1
        # else:
        # if root is None:
        #     return 0
        # else:
        #     count = 0
        #     if root.left is not None:
        #         count += self.pathSum(root.left,targetSum - root.val) + self.pathSum(root.left,targetSum)
        #     if root.right is not None:
        #         count += self.pathSum(root.right,targetSum - root.val) + self.pathSum(root.right,targetSum)
        #     if targetSum - root.val == 0:
        #         count += 1
        #         print(root, count)
        #     return count