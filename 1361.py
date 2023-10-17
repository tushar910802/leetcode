class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        """
        Validates whether the given node numbers form exactly one valid binary tree.

        Args:
            n: The number of nodes in the tree.
            leftChild: A list of the left child indices for each node.
            rightChild: A list of the right child indices for each node.

        Returns:
            True if the given nodes form exactly one valid binary tree, False otherwise.
        """

        graph = defaultdict(list)
        in_degree = [0] * n

        for node in range(n):
            left, right = leftChild[node], rightChild[node]
            if left != -1:
                graph[node].append(left)
                in_degree[left] += 1
            if right != -1:
                graph[node].append(right)
                in_degree[right] += 1

        root_candidates = [node for node in range(n) if in_degree[node] == 0]

        if len(root_candidates) != 1:
            return False  
        root = root_candidates[0]

        queue = [root]
        seen = set([root])

        while queue:
            node = queue.pop(0)
            if node in graph:
                for child in graph[node]:
                    if child in seen:
                        return False  
                    seen.add(child)
                    queue.append(child)

        return len(seen) == n

## 1361. Validate Binary Tree Nodes
