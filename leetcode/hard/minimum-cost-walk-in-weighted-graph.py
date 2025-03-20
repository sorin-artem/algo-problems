class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])

        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1


class Solution:
    def minimumCost(self, n: int, edges, query):
        uf = UnionFind(n)
        for u, v, w in edges:
            uf.union(u, v)

        component_cost = {}
        for u,v,w in edges:
            root = uf.find(u)
            if root not in component_cost:
                component_cost[root] = w
            else:
                component_cost[root] &= w

        res = []

        for src, dst in query:
            r1,r2 = uf.find(src), uf.find(dst)
            if r1 != r2:
                res.append(-1)
            else:
                res.append(component_cost[r1])

        return res