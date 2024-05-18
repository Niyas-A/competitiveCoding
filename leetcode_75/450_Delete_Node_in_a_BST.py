# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def helper(root, key):                
            if not root:
                return root
            if root.val < key:
                # print('going right')
                root.right = helper(root.right, key)
            elif root.val > key:
                # print('going left')
                root.left = helper(root.left, key)
            else:
                if not root.left:
                    # print("returning root.right")
                    # print(root.right)
                    return root.right
                if not root.right:
                    return root.left

                # find min node in right
                # if root.right is None and root.left is None:
                    # print('no leaf, returning None')
                    # return None
                else:
                    cur = root.right
                    while cur.left:
                        cur = cur.left
                    root.val = cur.val
                    # print('found min')
                    root.right = helper(root.right, root.val)
            # print('returning root')
            return root

        root = helper(root,key)
        print(root)
        return root
        
