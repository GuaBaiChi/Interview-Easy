# https://leetcode.com/problems/symmetric-tree/
# 101. Symmetric Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        # Return the function recursively...
        return self.isSame(root.left, root.right)

    def isSame(self, leftroot, rightroot):
        if leftroot == None and rightroot == None:
            return True
        if leftroot == None or rightroot == None:
            return False
        if leftroot.val != rightroot.val:
            return False

        return self.isSame(leftroot.left, rightroot.right) and self.isSame(
            leftroot.right, rightroot.left
        )


# Driver Code
# Let's construct the tree show in the above figure
# a
# [1, 2, 2, 3, 4, 4, 3]
# b
# [1, 2, 2, null, 3, null, 3]
# this will actually be produced as
# [1, 2, 2, 3, 3]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
solution = Solution()
# print("Symmetric" if solution.isSymmetric(root) == True else "Not symmetric")
if solution.isSymmetric(root) == True:
    print("Symmetric")
else:
    print("Not Symmetric")
