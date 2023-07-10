# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Finds the minimum depth of a binary tree.

        The minimum depth of a binary tree is the number of nodes on the shortest path from the root node to a leaf node.

        Parameters
        ----------
        root : Optional[TreeNode]
            A pointer to the root node of the binary tree.

        Returns
        -------
        int
            The minimum depth of the binary tree.
        """
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1



## 111. Minimum Depth of Binary Tree