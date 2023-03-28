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
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
solution = Solution()
print("Symmetric" if solution.isSymmetric(root) == True else "Not symmetric")

# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         # Special case...
#         if not root:
#             return true;
#         # Return the function recursively...
#         return self.isSame(root.left, root.right)
#     # A tree is called symmetric if the left subtree must be a mirror reflection of the right subtree...
#     def isSame(self, leftroot, rightroot):
#         # If both root nodes are null pointers, return true...
#         if leftroot == None and rightroot == None:
#             return True
#         # If exactly one of them is a null node, return false...
#         if leftroot == None or rightroot == None:
#             return False
#         # If root nodes haven't same value, return false...
#         if leftroot.val != rightroot.val:
#             return False
#         # Return true if the values of root nodes are same and left as well as right subtrees are symmetric...
#         return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)