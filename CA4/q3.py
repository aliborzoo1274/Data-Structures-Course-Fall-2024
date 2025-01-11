class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    ds = DisjointSet(n)
    
    for _ in range(m):
        a, b = map(int, input().split())
        ds.union(a, b)
    
    groups = {}
    for i in range(1, n+1):
        root = ds.find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)
    
    result = 0
    for root, positions in groups.items():
        values = [arr[i-1] for i in positions]
        matches = sum(1 for v in values if v in positions)
        result += matches
    
    print(result)

solve()