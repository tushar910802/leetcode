class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj_list = collections.defaultdict(list)

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        ans = [None]*n

        def traverse(node,parent):
            current_f = [0] * 26
            for child in adj_list[node]:
                if child != parent:
                    f = traverse(child,node)
                    for i in range(26):
                        current_f[i] += f[i]

            current_f[ord(labels[node]) - ord('a')] += 1
            ans[node] = current_f[ord(labels[node]) - ord('a')]

            return current_f
        traverse(0,-1)
        return ans