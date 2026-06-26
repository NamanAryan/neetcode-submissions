class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i : [] for i in range(n) }
        visit = set()
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = deque([node])
            visit.add(node)
            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)

        res = 0
        for node in range(n):
            if node not in visit:
                bfs(node)
                res += 1
        return res