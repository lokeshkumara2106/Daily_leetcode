class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        new_children = [[] for _ in range(n)]
        last = {}
        def build(node):
            c = s[node]
            old = last.get(c)
            # Find the closest ancestor with the same character
            new_parent = old if old is not None else parent[node]
            if node != 0:
                new_children[new_parent].append(node)
            # Store current node as the latest ancestor
            last[c] = node
            for child in children[node]:
                build(child)
            # Restore previous ancestor when DFS goes back
            if old is None:
                del last[c]
            else:
                last[c] = old
        build(0)
        # Calculate subtree sizes
        res = [1] * n
        def calculate(node):
            for child in new_children[node]:
                calculate(child)
                res[node] += res[child]
        calculate(0)
        return res