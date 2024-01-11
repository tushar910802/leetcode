# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the maximum difference between any two nodes in a binary tree, 
        considering the values of the ancestors during traversal.

        Parameters:
        - root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        - int: The maximum difference between any two nodes in the binary tree.

        Example:
        Consider a binary tree:
            8
            / \
        3   10
        / \    \
        1   6    14
            / \   /
        4   7  13

        maxAncestorDiff(root) should return 13 (|14 - 1| or |14 - 3|).

        Note:
        - The input binary tree is represented by TreeNode class.
        - TreeNode class has attributes: val, left, right.

        Complexity:
        - Time: O(N), where N is the number of nodes in the binary tree.
        - Space: O(H), where H is the height of the binary tree.
        """
        stack = [[root, [root.val, root.val]]]
        max_d = 0
        while stack:
            cur, ancestor = stack.pop()
            print(cur.val, ancestor)
            max_d = max(max_d, 
                        abs(cur.val - ancestor[0]), 
                        abs(cur.val - ancestor[1]))
            for child in[cur.left, cur.right]:
                if child:
                    stack.append([child, 
                                [min(cur.val, ancestor[0]), 
                                max(cur.val, ancestor[1])]])
        return max_d