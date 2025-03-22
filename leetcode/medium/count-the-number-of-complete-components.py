from collections import defaultdict
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(v, res):
            if v in visit:
                return
            visit.add(v)
            res.append(v)
            for neighbor in adj[v]:
                dfs(neighbor, res)
            return res
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        res = 0
        visit = set()
        for v in range(n):
            if v in visit:
                continue
            component = dfs(v, [])
            flag = True
            for v2 in component:
                if len(component) - 1 != len(adj[v2]):
                    flag = False
                    break
            if flag:
                res += 1
        return res
