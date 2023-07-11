# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        def dfs(parent,child):
            if child is None: return
            if parent and child:
                graph[child.val].append(parent.val)
                graph[parent.val].append(child.val)
            dfs(child, child.left)
            dfs(child, child.right)
            return
        
        dfs(None,root)
        
        queue = collections.deque([target.val])
        visited=set()
        visited.add(target.val)
        while K:
            for i in range(len(queue)):
                parent=queue.popleft()
                visited.add(parent)
                for child in graph[parent]:
                    if child not in visited:
                        queue.append(child)
            K-=1
        return list(queue)